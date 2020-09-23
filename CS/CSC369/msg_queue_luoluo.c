/*
 * This code is provided solely for the personal and private use of students
 * taking the CSC369H course at the University of Toronto. Copying for purposes
 * other than this use is expressly prohibited. All forms of distribution of
 * this code, including but not limited to public repositories on GitHub,
 * GitLab, Bitbucket, or any other online platform, whether as given or with
 * any changes, are expressly prohibited.
 *
 * Authors: Alexey Khrabrov, Andrew Pelegris, Karen Reid
 *
 * All of the files in this directory and all subdirectories are:
 * Copyright (c) 2019 Karen Reid
 */

/**
 * CSC369 Assignment 2 - Message queue implementation.
 *
 * You may not use the pthread library directly. Instead you must use the
 * functions and types available in sync.h.
 */

#include <stdio.h>
#include <assert.h>
#include <errno.h>
#include <stdlib.h>

#include "errors.h"
#include "list.h"
#include "msg_queue.h"
#include "ring_buffer.h"
#include "sync.h"


typedef struct watching_thread {
	msg_queue_pollfd mq_fd;
	int actions_num;
	cond_t* has_action;
	mutex_t* watching_thread_lock;
	list_entry entry;
} watching_thread;


// Message queue implementation backend
typedef struct mq_backend {
	// Ring buffer for storing the messages
	ring_buffer buffer;
	// Reference count
	size_t refs;
	// Number of handles open for reads
	size_t readers;
	// Number of handles open for writes
	size_t writers;
	// Set to true when all the reader handles have been closed. Starts false
	// when they haven't been opened yet.
	bool no_readers;
	// Set to true when all the writer handles have been closed. Starts false
	// when they haven't been opened yet.
	bool no_writers;
	//TODO - Add the necessary synchronization variables.
	mutex_t r_w_countLock;
	mutex_t bufferLock;
	cond_t bufferNotFull;
	cond_t bufferNotEmpty;
	struct list_head wait_list;

} mq_backend;



static int mq_init(mq_backend *mq, size_t capacity)
{
	fprintf(stderr, "\n\n--------  Enter mq_init  ---------\n");
	if (ring_buffer_init(&mq->buffer, capacity) < 0) return -1;
	mq->buffer.size = capacity;
	fprintf(stderr, "--------  rb inited, buffer size: %zu  ---------\n", mq->buffer.size);
	mq->refs = 0;
	mq->readers = 0;
	mq->writers = 0;
	mq->no_readers = false;
	mq->no_writers = false;
	//TODO
	fprintf(stderr, "mq_init TODO\n");
	mutex_init(&(mq->r_w_countLock));
	mutex_init(&(mq->bufferLock));
	cond_init(&(mq->bufferNotFull));
	cond_init(&(mq->bufferNotEmpty));
	list_entry_init(&(mq->wait_list.head));
	list_init(&(mq->wait_list));
	fprintf(stderr, "@@@@@ wait list address: %p\n", (void*)&(mq->wait_list));
	fprintf(stderr, "@@@@@ wait list head address: %p\n", (void*)&(mq->wait_list.head));
	fprintf(stderr, "%d\n", (void*)&(mq->wait_list.head) == (void*)&(mq->wait_list));
	fprintf(stderr, "mq_init TODO done\n");
	fprintf(stderr, "--------  end of mq_init  ---------\n\n");

	return 0;
}

static void mq_destroy(mq_backend *mq)
{
		printf("\n-------  Enter mq_destroy  --------\n");

	assert(mq->refs == 0);
	assert(mq->readers == 0);
	assert(mq->writers == 0);

	//TODO
	mutex_destroy(&(mq->r_w_countLock));
	printf("r_w_countLock destroyed\n");
	mutex_destroy(&(mq->bufferLock));
		printf("bufferLock destroyed\n");
	cond_destroy(&(mq->bufferNotFull));
	printf("bufferNotFull destroyed\n");
	cond_destroy(&(mq->bufferNotEmpty));
		printf("bufferNotEmpty destroyed\n");
	mq->no_readers = true;
	mq->no_writers = true;
	ring_buffer_destroy(&mq->buffer);
	printf("ring buffer destroyed\n");
	// mutex_destroy(&(mq->list_lock));
	// printf("list_lock destroyed\n");
	printf("-------  Exit mq_destroy  --------\n\n");

}






// ---------- msg queue handle  (queue backend ptr, handle flag) ---------------

#define ALL_FLAGS (MSG_QUEUE_READER | MSG_QUEUE_WRITER | MSG_QUEUE_NONBLOCK)
#define ALL_POLL_FLAGS (MQPOLL_READABLE | MQPOLL_WRITABLE | MQPOLL_NOREADERS | MQPOLL_NOWRITERS)

// Message queue handle is a combination of the pointer to the queue backend and
// the handle flags. The pointer is always aligned on 8 bytes - its 3 least
// significant bits are always 0. This allows us to store the flags within the
// same word-sized value as the pointer by ORing the pointer with the flag bits.

//  从 queue handle 中找出 backend
// Get queue backend pointer from the queue handle
static mq_backend *get_backend(msg_queue_t queue)
{
	mq_backend *mq = (mq_backend*)(queue & ~ALL_FLAGS);
	assert(mq);
	return mq;
}


//  从 queue handle 中找出 handle flag
// Get handle flags from the queue handle
static int get_flags(msg_queue_t queue)
{
	return (int)(queue & ALL_FLAGS);
}


// Create a queue handle for given backend pointer and handle flags
static msg_queue_t make_handle(mq_backend *mq, int flags)
{
	fprintf(stderr, "\n\n----------  Enter make_handle  ---------\n");
	assert(((uintptr_t)mq & ALL_FLAGS) == 0);
	assert((flags & ~ALL_FLAGS) == 0);
		printf(" queue: %lu created\n", (uintptr_t)mq | flags);
	fprintf(stderr, "----------  Exit make_handle  ---------\n\n");
	return (uintptr_t)mq | flags;
}



static msg_queue_t mq_open(mq_backend *mq, int flags)
{
	fprintf(stderr, "\n\n----------  Enter mq_open  ---------\n");
	++mq->refs;
	if (flags & MSG_QUEUE_READER) {
		++mq->readers;
		mq->no_readers = false;
	}
	if (flags & MSG_QUEUE_WRITER) {
		++mq->writers;
		mq->no_writers = false;
	}
		fprintf(stderr, " refs: %zu  Readers : %zu  writters: %zu\n", mq->refs, mq->readers, mq->writers);
		fprintf(stderr, "----------  End of mq_open  ---------\n\n");
	return make_handle(mq, flags);   // return the handle on this mq
}



// Returns true if this was the last handle
static bool mq_close(mq_backend *mq, int flags)
{
		printf("\n\n------ Enter mq_close ------\n");
	assert(mq->refs != 0);
	assert(mq->refs >= mq->readers);
	assert(mq->refs >= mq->writers);
	if (flags & MSG_QUEUE_READER) {
		if (--mq->readers == 0) mq->no_readers = true;
	}
	if (flags & MSG_QUEUE_WRITER) {
		if (--mq->writers == 0) mq->no_writers = true;
	}
	if (--mq->refs == 0) {
		assert(mq->readers == 0);
		assert(mq->writers == 0);
		return true;
	}
	printf("handle closed\n");
	fprintf(stderr, " refs: %zu  Readers : %zu  writters: %zu\n", mq->refs, mq->readers, mq->writers);
	printf("------ Exit mq_close ------\n\n");
	return false;
}




msg_queue_t msg_queue_create(size_t capacity, int flags)
{

	fprintf(stderr, "\n\n----------  Enter msg_queue_create  ---------\n");
	fprintf(stderr, "\n\n capacity is %zu, flags : %d\n", capacity, flags);
	// check if flags is valid
	if (flags & ~ALL_FLAGS) {
		errno = EINVAL;
		report_error("msg_queue_create");
		return MSG_QUEUE_NULL;
	}
	// allocate memory for mq_backend
	mq_backend *mq = (mq_backend*)malloc(sizeof(mq_backend));
	fprintf(stderr, "mq_backend space malloced\n");
	if (mq == NULL) {
		report_error("malloc");
		return MSG_QUEUE_NULL;
	}
	fprintf(stderr, "mq not null\n");
	// Result of malloc() is always aligned on 8 bytes, allowing us to use the
	// 3 least significant bits of the handle to store the 3 bits of flags
	// check if last 3 bits are 000
	assert(((uintptr_t)mq & ALL_FLAGS) == 0);
	// init mq_backend
	if (mq_init(mq, capacity) < 0) {
		fprintf(stderr, "mq_init false\n");
		// Preserve errno value that can be changed by free()
		int e = errno;
		free(mq);
		errno = e;
		return MSG_QUEUE_NULL;
	}
	fprintf(stderr, " msg queue inited \n");
		fprintf(stderr, "----------  End of msg_queue_create  ---------\n\n");
	// return handle on mq_backend
	return mq_open(mq, flags);
}




msg_queue_t msg_queue_open(msg_queue_t queue, int flags)
{
	printf(" \n\n--------  Enter msg_queue_open  --------\n");
	// check if queue is a valid queue handle
	if (!queue) {
		errno = EBADF;
		report_error("msg_queue_open");
		return MSG_QUEUE_NULL;
	}
	printf(" a valid queue \n");
	// check if flag is valid
	if (flags & ~ALL_FLAGS) {
		errno = EINVAL;
		report_error("msg_queue_open");
		return MSG_QUEUE_NULL;
	}
	printf(" a valid flag \n");
	// get queue backend from queue handle
	mq_backend *mq = get_backend(queue);
	printf(" got msg_queue_backend \n");
	//TODO
	printf(" wait lock of r_w \n");
	mutex_lock(&(mq->r_w_countLock));
	printf(" got lock of r_w \n");
	// 设置 handle 的 flag， 得到新的 handle
	msg_queue_t new_handle = mq_open(mq, flags);
	printf(" got new handle and return it \n");
	printf(" release lock of r_w \n");
	mutex_unlock(&(mq->r_w_countLock));
	printf("\n --------  Exit msg_queue_open  --------\n\n");
	return new_handle;
}




int msg_queue_close(msg_queue_t *queue)
{
		printf("\n\n --------  Enter msg_queue_close  --------\n");
	// check if queue handle is NULL
	if (!*queue) {
		errno = EBADF;
		report_error("msg_queue_close");
		return -1;
	}
	// get queue backend from queue handle
	mq_backend *mq = get_backend(*queue);
	//TODO
	printf("wait lock for w_r\n");
	mutex_lock(&(mq->r_w_countLock));
	printf("got lock for w_r\n");
	// close flags of handle on queue backend
	if (mq_close(mq, get_flags(*queue))) {
		printf("release lock for w_r\n");
		mutex_unlock(&(mq->r_w_countLock));
		// Closed last handle; destroy the queue

		printf("~~~~~~ closing the last handle\n");

		mq_destroy(mq);
		free(mq);
		*queue = MSG_QUEUE_NULL;
		return 0;
	}
	printf("~~~~~~ not the last handle\n");

	if(mq->no_readers && !mq->no_writers){
		printf("0 readers & >0 writers\n");
	printf("###### closer Begin to iterate wait threads list\n");
			printf("wait for bufferLock\n");
		mutex_lock(&(mq->bufferLock));
		printf("got bufferLock\n");
		list_entry*  wait_handle_entry_ptr = NULL;
		list_for_each( wait_handle_entry_ptr, &(mq->wait_list)){
					 struct watching_thread* watching_thread = container_of(wait_handle_entry_ptr, struct watching_thread, entry);
					 if(watching_thread){
					 	mutex_lock(watching_thread->watching_thread_lock);
					 	if((watching_thread->mq_fd.events & MQPOLL_WRITABLE) || (watching_thread->mq_fd.events & MQPOLL_NOREADERS)){
						 	printf("###### closer %lu got watching_thread queue %lu\n", *queue, watching_thread->mq_fd.queue);
							watching_thread->mq_fd.revents = watching_thread->mq_fd.revents | MQPOLL_NOREADERS;
							printf("###### closer change revents to NOREADERS\n");
							// watching_thread->actions_num++;
							cond_signal(watching_thread->has_action);
							printf("###### closer signaled NOREADERS\n");
					 	}
					 	mutex_unlock(watching_thread->watching_thread_lock);
				 	}
		}
		printf("release for bufferLock\n");
		mutex_unlock(&(mq->bufferLock));
	}

	if(mq->no_writers && !mq->no_readers){
		printf(">0 readers & 0 writers\n");
		printf("wait for bufferLock\n");
		mutex_lock(&(mq->bufferLock));
		printf("###### closer Begin to iterate wait threads list\n");
		list_entry*  wait_handle_entry_ptr = NULL;
		list_for_each( wait_handle_entry_ptr, &(mq->wait_list)){
			struct watching_thread* watching_thread = container_of(wait_handle_entry_ptr, struct watching_thread, entry);
			if(watching_thread){
				mutex_lock(watching_thread->watching_thread_lock);
				if(watching_thread->mq_fd.events & (MQPOLL_READABLE | MQPOLL_NOWRITERS)){
					printf("###### closer %lu got watching_thread queue %lu\n", *queue, watching_thread->mq_fd.queue);
			 		watching_thread->mq_fd.revents = watching_thread->mq_fd.revents | MQPOLL_NOWRITERS;
			 		printf("###### closer change revents to NOWRITERS\n");
			 		// watching_thread->actions_num++;
			 		cond_signal(watching_thread->has_action);
			 		printf("###### closer signaled NOWRITERS\n");
				}
				mutex_unlock(watching_thread->watching_thread_lock);
			}
		}
		printf("release bufferLock\n");
		mutex_unlock(&(mq->bufferLock));
	}

	printf("release lock for w_r\n");
	mutex_unlock(&(mq->r_w_countLock));
	//TODO
	*queue = MSG_QUEUE_NULL;
	printf(" --------  Exit msg_queue_close  --------\n\n");
	// destroy success
	return 0;
}




ssize_t msg_queue_read(msg_queue_t queue, void *buffer, size_t count)
{
	printf("\n\n-------- %lu Enter msg_queue_read  --------\n", queue);
	//TODO
	// get queue backend from queue handle
	mq_backend *mq = get_backend(queue);
	printf("reader %lu wait lock for buffer\n", queue);
	mutex_lock(&(mq->bufferLock));
	printf("reader %lu got lock for buffer\n", queue);

	// check if queue handle is NULL
	if (!queue) {
		errno = EBADF;
		report_error("msg_queue_close");
		return -1;}
	if(get_flags(queue) & MSG_QUEUE_NONBLOCK){ // non-blocking flag, EAGAIN
		errno = EAGAIN;
		mutex_unlock(&(mq->bufferLock));
		return -1;}
	if((mq->buffer).size < count){ // buffer to small, EMSGSIZE
		errno = EMSGSIZE;
		mutex_unlock(&(mq->bufferLock));
		return -1;}



	while((mq->buffer).head == (mq->buffer).tail && (mq->buffer).full == false){ // buffer empty
		printf("buffer empty\n");
		printf("reader %lu wait r_w_countLock\n", queue);
		mutex_lock(&(mq->r_w_countLock));
		printf("reader %lu got r_w_countLock\n", queue);
		if(mq->no_writers == true){ // buffer empty and all writers closed, return 0
			printf("all writers closed, reader release lock, return 0\n");
			mutex_unlock(&(mq->r_w_countLock));
			printf("reader %lu release r_w_countLock\n", queue);
			mutex_unlock(&(mq->bufferLock));
				printf("reader %lu release bufferLock\n", queue);
			return 0;
		}
		mutex_unlock(&(mq->r_w_countLock));
		printf("reader %lu release r_w_countLock\n", queue);
		printf("reader %lu wait bufferNotEmpty, released bufferlock\n", queue);
		cond_wait(&(mq->bufferNotEmpty), &(mq->bufferLock));
		printf("reader %lu got bufferNotEmpty, got bufferlock\n", queue);
	}
	printf("buffer not empty, reader got buffer lock\n");
	bool enough_msg = ring_buffer_read(&(mq->buffer), buffer, count);
	if(enough_msg == false){ // not enough msg, wait for signal after writing, release bufferLock
		// exit while loop, got buffer lock and read successfully
		printf("read but not enough msg, reader %lu wait for signal after writing\n", queue);
		cond_signal(&(mq->bufferNotFull));
		printf("reader %lu signal writters buffer not full\n", queue);
		mutex_unlock(&(mq->bufferLock));
		printf("reader %lu release bufferLock\n", queue);
		int negated = count - ring_buffer_used(&(mq->buffer));
		printf("stop read, return negated\n");
		return negated;
	}
	printf("reader %lu readed %zu bytes\n", queue, count);
	// exit while loop, got buffer lock and read successfully

		printf("###### reader Begin to iterate wait threads list for queue %lu\n", queue);
  		list_entry*  wait_handle_entry_ptr = NULL;
  	  list_for_each( wait_handle_entry_ptr, &(mq->wait_list)){
  	         struct watching_thread* watching_thread = container_of(wait_handle_entry_ptr, struct watching_thread, entry);
						 if(watching_thread){
						 mutex_lock(watching_thread->watching_thread_lock);
						 if(watching_thread->mq_fd.events & MQPOLL_WRITABLE){
							 printf("###### reader %lu got watching_thread queue %lu\n", queue, watching_thread->mq_fd.queue);
							 printf("###### reader change revents to WRITABLE\n");
							 	watching_thread->mq_fd.revents = watching_thread->mq_fd.revents | MQPOLL_WRITABLE;
								// watching_thread->actions_num++;
								cond_signal(watching_thread->has_action);
								printf("###### signaled poll WRITABLE\n");
								// printf("###### thread action_num is%d\n", watching_thread->actions_num);
						 }
						 mutex_unlock(watching_thread->watching_thread_lock);
					 }
  		}

	cond_signal(&(mq->bufferNotFull));
	printf("reader %lu signal writters buffer not full\n", queue);
	mutex_unlock(&(mq->bufferLock));
	printf("reader %lu release lock for buffer\n", queue);
	printf("-------- %lu Exit msg_queue_read  --------\n\n", queue);
	return count;

}



int msg_queue_write(msg_queue_t queue, const void *buffer, size_t count)
{
		printf("\n\n-------- %lu Enter msg_queue_write --------\n", queue);
	//TODO

		// get queue backend from queue handle
		mq_backend *mq = get_backend(queue);
	// check if queue handle is NULL
	if (!queue) {
		errno = EBADF;
		report_error("msg_queue_close\n");
		return -1;}

	printf("writer %lu wait r_w_countLock\n", queue);
	mutex_lock(&(mq->r_w_countLock));
	printf("writer %lu got r_w_countLock\n", queue);
	if(mq->no_readers){ // no readers error, EPIPE
		errno = EPIPE;
		report_error("no readers error\n");
		mutex_unlock(&(mq->r_w_countLock));
		printf("writer %lu release r_w_countLock\n", queue);
		return -1;}
		mutex_unlock(&(mq->r_w_countLock));
		printf("writer %lu release r_w_countLock\n", queue);

	printf("writer %lu wait lock for buffer\n", queue);
	mutex_lock(&(mq->bufferLock));
	printf("writer %lu got lock for buffer\n", queue);
	if((mq->buffer).size < count){ // buffer to small, EMSGSIZE
		errno = EMSGSIZE;
		printf("buffer size: %lu, count: %lu", (mq->buffer).size, count);
		report_error("buffer size: to small\n");
		mutex_unlock(&(mq->bufferLock));
		printf("writer %lu release lock for buffer\n", queue);
		return -1;}
		mutex_unlock(&(mq->bufferLock));
		printf("writer %lu release lock for buffer\n", queue);

	if(count == 0){ // zero length mssg, EINVAL
		errno = EINVAL;
		report_error("zero length mssg\n");
		return -1;}
	if(get_flags(queue) & MSG_QUEUE_NONBLOCK){ // non-blocking flag, EAGAIN
		errno = EAGAIN;
		report_error("non-blocking flag\n");
		return -1;}

		printf("writer %lu wait lock for buffer\n", queue);
		mutex_lock(&(mq->bufferLock));
		printf("writer %lu got lock for buffer\n", queue);
		printf("Error checked and begin write\n");
	while((mq->buffer).head == (mq->buffer).tail && (mq->buffer).full == true){
		printf("buffer full, writer %lu wait bufferNotFull, release bufferlock\n", queue);
		cond_wait(&(mq->bufferNotFull), &(mq->bufferLock));
	}
	printf("buffer not full, writer %lu got bufferlock, can write\n", queue);

	bool enough_space = ring_buffer_write(&(mq->buffer), buffer, count);
	while(enough_space == false){ // not enough space, wait for signal after reading, release bufferLock
		printf("space not enough, writer %lu wait bufferNotFull, release buffer lock\n", queue);
		cond_wait(&(mq->bufferNotFull), &(mq->bufferLock));
		enough_space = ring_buffer_write(&(mq->buffer), buffer, count);
	}
	printf("space enough, already wrote\n");

		printf("###### writer Begin to iterate wait threads list for queue %lu\n", queue);
			list_entry* wait_handle_entry_ptr = NULL;
  	  list_for_each( wait_handle_entry_ptr, &(mq->wait_list)){
							printf("@@@@@ entry address: %p\n", (void*)wait_handle_entry_ptr);
  	         struct watching_thread* watching_thread = container_of(wait_handle_entry_ptr, struct watching_thread, entry);
						 if(watching_thread){
						 mutex_lock(watching_thread->watching_thread_lock);
						 printf("###### got watching_thread_lock\n");
						 		if(watching_thread->mq_fd.events & MQPOLL_READABLE){
							 		printf("###### writer %lu got watching_thread queue %lu\n", queue, watching_thread->mq_fd.queue);
							 		printf("###### change revents to READABLE\n");
							 		watching_thread->mq_fd.revents = watching_thread->mq_fd.revents | MQPOLL_READABLE;
									printf("###### revents : %d\n", watching_thread->mq_fd.revents);
									// watching_thread->actions_num++;
									cond_signal(watching_thread->has_action);
									printf("###### signaled poll READABLE\n");
									// printf("###### thread action_num is%d\n", watching_thread->actions_num);
						 		}
						  mutex_unlock(watching_thread->watching_thread_lock);
							printf("###### released watching_thread_lock\n");
						}
  		}

	// release lock, signal reader
	cond_signal(&(mq->bufferNotEmpty));
	printf("writer %lu notify bufferNotEmpty\n", queue);
	mutex_unlock(&(mq->bufferLock));
	printf("writer %lu released lock for buffer\n", queue);

	printf("-------- %lu Exit msg_queue_write --------\n\n", queue);
	return 0;

}





int msg_queue_poll(msg_queue_pollfd *fds, size_t nfds)
{
		printf("\n\n!!!!!!! Enter msg_queue_poll !!!!!!!!\n");
	//TODO

	if(nfds == 0){
		errno = EINVAL;
		report_error("event flags invalid");
		return -1;
	}

	// check if thread alraedy exists in wait list of some queues
	// struct watching_thread* curr_watching_thread = NULL;

	cond_t* thread_active = malloc(sizeof(cond_t));
	mutex_t* thread_lock = malloc(sizeof(mutex_t));
	// init thread node
	cond_init(thread_active);
	mutex_init(thread_lock);

	struct list_entry* entry_array[nfds];
	struct watching_thread* thread_array[nfds];

	for(size_t i = 0; i < nfds; i++){// get queue backend from queue handle
		// mq_backend *mq = get_backend(fds[i].queue);
		if(fds[i].events & ~ALL_POLL_FLAGS){
			errno = EINVAL;
			report_error("event flags invalid");
			return -1;
		}
		if(((fds[i].events & MQPOLL_READABLE) && (get_flags(fds[i].queue) & MSG_QUEUE_WRITER)) ||
		((fds[i].events & MQPOLL_WRITABLE) && (get_flags(fds[i].queue) & MSG_QUEUE_READER))){
				errno = EINVAL;
				report_error("event flags invalid");
				return -1;
		}

		entry_array[i] = malloc(sizeof(struct list_entry));
		list_entry_init(entry_array[i]);
		thread_array[i] = malloc(sizeof(struct watching_thread));
		thread_array[i]->has_action = thread_active;
		thread_array[i]->watching_thread_lock = thread_lock;
		thread_array[i]->actions_num = 0;
	}



	int count = 0;
	for(unsigned long i = 0; i < nfds; i++){
		// get queue backend from queue handle
		mq_backend *mq = get_backend(fds[i].queue);

		printf("!!!!!!! wait r_w_countLock\n");
		mutex_lock(&(mq->r_w_countLock));
		printf("!!!!!!! got r_w_countLock\n");
		// check if events on queue already been active
		printf("!!!!!!! fd%zu wait buffer lock of queue %lu\n", i, fds[i].queue);
		mutex_lock(&(mq->bufferLock));
		printf("!!!!!!! fd%zu got buffer lock of queue %lu\n", i, fds[i].queue);

		if(fds[i].events & MQPOLL_READABLE && ring_buffer_used(&(mq->buffer)) > 0){
			printf("!!!!!!! READABLE already active\n");
			if(mq->no_writers){
			     fds[i].revents = fds[i].revents | MQPOLL_NOWRITERS;
			 }
			 fds[i].revents = fds[i].revents | MQPOLL_READABLE;
			 count += 1;
		 }
		if(fds[i].events & MQPOLL_WRITABLE && ring_buffer_free(&(mq->buffer)) > 0){
            printf("!!!!!!! WRITABLE already active\n");
            if(mq->no_readers){
                fds[i].revents = fds[i].revents | MQPOLL_NOREADERS;
            }
            fds[i].revents = fds[i].revents | MQPOLL_WRITABLE;
            count += 1;
    }

    if(mq->no_writers && mq->no_readers){
            printf("!!!!!!! NOWRITERS/NOWRITERS already active\n");
            fds[i].revents = fds[i].revents | MQPOLL_NOWRITERS;
            fds[i].revents = fds[i].revents | MQPOLL_NOREADERS;
            count += 1;
    }
    else{
          if(mq->no_writers){
                printf("!!!!!!! NOWRITERS already active\n");
                fds[i].revents = fds[i].revents | MQPOLL_NOWRITERS;
                count += 1;
            }
            if(mq->no_readers){
                printf("!!!!!!! NOREADERS already active\n");
                fds[i].revents = fds[i].revents | MQPOLL_NOREADERS;
                count += 1;
    			}
		}

		mutex_unlock(&(mq->r_w_countLock));
		printf("!!!!!!! release r_w_countLock\n");


	if(count==0){
					printf("!!!!!!! add thread into wait list of queue %lu\n", fds[i].queue);
					printf("!!!!!!! wait watching_thread_lock\n");
					mutex_lock(thread_array[i]->watching_thread_lock);
					printf("!!!!!!! got watching_thread_lock\n");
					thread_array[i]->mq_fd = fds[i];
					thread_array[i]->entry = *(entry_array[i]);

					printf("!!!!!!! handle %lu added in wait_list of queue %lu \n", thread_array[i]->mq_fd.queue, fds[i].queue);
					mutex_unlock(thread_array[i]->watching_thread_lock);
					printf("!!!!!!! release watching_thread_lock\n");
	}

	mutex_unlock(&(mq->bufferLock));
	printf("!!!!!!! fd%zu release buffer lock of queue %lu\n", i, fds[i].queue);
}

if(count == 0){
	printf("!!!!!!! wait watching_thread_lock\n");
	mutex_lock(thread_lock);
	printf("!!!!!!! got watching_thread_lock\n");
	printf("!!!!!!! wait for action signal, release thread_lock\n");
	cond_wait(thread_active, thread_lock);
	printf("!!!!! got watching_thread_lock, got READABLE signal\n");
	count++;
	// for(size_t i = 0; i < nfds; i++){
	// 	mq_backend *mq = get_backend(fds[i].queue);
	// 	mutex_lock(&(mq->bufferLock));
	// 	list_del(&(mq->wait_list), entry_array[i]);
	// 	mutex_unlock(&(mq->bufferLock));
	// }
	// for(size_t i = 0; i < nfds; i++){
	// 	mq_backend* mq = get_backend(fds[i].queue);
	// 	mutex_lock(&mq->bufferLock);
	// 	list_del(&mq->wait_list, entry_array[i]);
	// 	mutex_unlock(&(mq->bufferLock));
	// }
	mutex_unlock(thread_lock);
	printf("!!!!!!! thread_lock\n");
}
	// mutex_destroy(thread_lock);
	// cond_destroy(thread_active);
	// free(thread_active);
	// free(thread_lock);
	// for(size_t i= 0; i < nfds; i++) {
	// 	free(entry_array[i]);
	// 	free(thread_array[i]);
	// }
	return count;


}
