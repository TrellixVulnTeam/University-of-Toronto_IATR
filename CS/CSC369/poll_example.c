
static inline unsigned int do_pollfd(struct pollfd *pollfd, poll_table *pwait)
{
    unsigned int mask;
    int fd;
    mask = 0;
    fd = pollfd->fd;
    if (fd >= 0) {
        int fput_needed;
        struct file * file;
        // 取得fd对应的文件结构体
        file = fget_light(fd, &fput_needed);
        mask = POLLNVAL;
        if (file != NULL) {
            // 如果没有 f_op 或 f_op->poll 则认为文件始终处于就绪状态.
            mask = DEFAULT_POLLMASK;
            if (file->f_op && file->f_op->poll) {
                if (pwait) {
                    // 设置关注的事件掩码
                    pwait->key = pollfd->events | POLLERR | POLLHUP;
                }
                // 注册回调函数，并返回当前就绪状态，就绪后会调用pollwake
                mask = file->f_op->poll(file, pwait);
            }
            mask &= pollfd->events | POLLERR | POLLHUP; // 移除不需要的状态掩码
            fput_light(file, fput_needed);// 释放文件
        }
    }
    pollfd->revents = mask; // 更新事件状态
    return mask;
}  


static int do_poll(unsigned int nfds,  struct poll_list *list,
                   struct poll_wqueues *wait, struct timespec *end_time)
{
    poll_table* pt = &wait->pt;
    ktime_t expire, *to = NULL;
    int timed_out = 0, count = 0;
    unsigned long slack = 0;
    if (end_time && !end_time->tv_sec && !end_time->tv_nsec) {
        // 已经超时,直接遍历所有文件描述符, 然后返回
        pt = NULL;
        timed_out = 1;
    }
    if (end_time && !timed_out) {
        // 估计进程等待时间，纳秒
        slack = select_estimate_accuracy(end_time);
    }

    // 遍历文件，为每个文件的等待队列添加唤醒函数(pollwake)
    for (;;) {
        struct poll_list *walk;
        for (walk = list; walk != NULL; walk = walk->next) {
            struct pollfd * pfd, * pfd_end;
            pfd = walk->entries;
            pfd_end = pfd + walk->len;
            for (; pfd != pfd_end; pfd++) {
                // do_pollfd 会向文件对应的wait queue 中添加节点
                // 和回调函数(如果 pt 不为空)
                // 并检查当前文件状态并设置返回的掩码
                if (do_pollfd(pfd, pt)) {
                    // 该文件已经准备好了.
                    // 不需要向后面文件的wait queue 中添加唤醒函数了.
                    count++;
                    pt = NULL;
                }
            }
        }
        // 下次循环的时候不需要向文件的wait queue 中添加节点,
        // 因为前面的循环已经把该添加的都添加了
        pt = NULL;

        // 第一次遍历没有发现ready的文件
        if (!count) {
            count = wait->error;
            // 有信号产生
            if (signal_pending(current)) {
                count = -EINTR;
            }
        }

        // 有ready的文件或已经超时
        if (count || timed_out) {
            break;
        }
        // 转换为内核时间
        if (end_time && !to) {
            expire = timespec_to_ktime(*end_time);
            to = &expire;
        }
        // 等待事件就绪, 如果有事件发生或超时，就再循
        // 环一遍，取得事件状态掩码并计数,
        // 注意此次循环中, 文件 wait queue 中的节点依然存在
        if (!poll_schedule_timeout(wait, TASK_INTERRUPTIBLE, to, slack)) {
            timed_out = 1;
        }
    }
    return count;
}
