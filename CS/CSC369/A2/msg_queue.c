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
 * Copyright (c) 2019, 2020 Karen Reid
 */

/**
 * CSC369 Assignment 2 - Message queue implementation.
 *
 * You may not use the pthread library directly. Instead you must use the
 * functions and types available in sync.h.
 */

#include <assert.h>

#include <errno.h>

#include <stdlib.h>

#include <stdio.h>

#include "errors.h"

#include "list.h"

#include "msg_queue.h"

#include "ring_buffer.h"


typedef struct message {
  int data;
}
message;

typedef struct fd_poll_wrapper {
  mutex_t * mutex;
  cond_t * cond;
  bool * signal;
  struct list_entry entry;
  int request_event;
}
fd_poll_wrapper;

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
  
  //TODO: add necessary synchronization primitives, as well as data structures
  //      needed to implement the msg_queue_poll() functionality
  cond_t cond_read;
  cond_t cond_write;
  
  mutex_t mutex;
  
  struct list_head * linked_list;
  // add one pair of bool variable to indicate if ever has reader or writer?
  bool reader_existed;
  bool writer_existed;
}
mq_backend;

static int mq_init(mq_backend * mq, size_t capacity) {
  if (ring_buffer_init( & mq -> buffer, capacity) < 0) {
    return -1;
  }
  
  mq -> refs = 0;
  
  mq -> readers = 0;
  mq -> writers = 0;
  
  mq -> no_readers = false;
  mq -> no_writers = false;
  
  //TODO: initialize remaining fields (synchronization primitives, etc.)
  mq -> reader_existed = false;
  mq -> writer_existed = false;
  
  // initialize two conditional variables and one lock
  cond_init( & mq -> cond_read);
  
  cond_init( & mq -> cond_write);
  
  mutex_init( & mq -> mutex);
  
  // initialize the linked-list head
  mq -> linked_list = (struct list_head * ) malloc(sizeof(struct list_head));
  
  if (mq -> linked_list == NULL) {
    report_error("malloc ");
    return -1;
  }
  
  list_init(mq -> linked_list);
  return 0;
}

static void mq_destroy(mq_backend * mq) {
  assert(mq -> refs == 0);
  assert(mq -> readers == 0);
  assert(mq -> writers == 0);
  
  //TODO: cleanup remaining fields (synchronization primitives, etc.)
  // two conditional variable, one lock, free linkedlist
  cond_destroy( & mq -> cond_read);
  cond_destroy( & mq -> cond_write);
  mutex_destroy( & mq -> mutex);
  list_del(mq -> linked_list, & ((mq -> linked_list) -> head));
  validator_destroy( & ((mq -> linked_list) -> validator));
  free(mq -> linked_list);
  ring_buffer_destroy( & mq -> buffer);
}

#define ALL_FLAGS (MSG_QUEUE_READER | MSG_QUEUE_WRITER | MSG_QUEUE_NONBLOCK)
#define ALL_EVENT_FLAGS (MQPOLL_READABLE | MQPOLL_WRITABLE | MQPOLL_NOREADERS | MQPOLL_NOWRITERS)

// Message queue handle is a combination of the pointer to the queue backend and
// the handle flags. The pointer is always aligned on 8 bytes - its 3 least
// significant bits are always 0. This allows us to store the flags within the
// same word-sized value as the pointer by ORing the pointer with the flag bits.

// Get queue backend pointer from the queue handle
static mq_backend * get_backend(msg_queue_t queue) {
  mq_backend * mq = (mq_backend * )(queue & ~ALL_FLAGS);
  assert(mq);
  return mq;
}

// Get handle flags from the queue handle
static int get_flags(msg_queue_t queue) {
  return (int)(queue & ALL_FLAGS);
}

// Create a queue handle for given backend pointer and handle flags
static msg_queue_t make_handle(mq_backend * mq, int flags) {
  assert(((uintptr_t) mq & ALL_FLAGS) == 0);
  assert((flags & ~ALL_FLAGS) == 0);
  return (uintptr_t) mq | flags;
}

static msg_queue_t mq_open(mq_backend * mq, int flags) {
  ++mq -> refs;
  
  if (flags & MSG_QUEUE_READER) {
    ++mq -> readers;
    mq -> no_readers = false;
    mq -> reader_existed = true;
  }
  if (flags & MSG_QUEUE_WRITER) {
    ++mq -> writers;
    mq -> no_writers = false;
    mq -> writer_existed = true;
  }
  
  return make_handle(mq, flags);
}

// Returns true if this was the last handle
static bool mq_close(mq_backend * mq, int flags) {
  assert(mq -> refs != 0);
  assert(mq -> refs >= mq -> readers);
  assert(mq -> refs >= mq -> writers);
  
  if ((flags & MSG_QUEUE_READER) && (--mq -> readers == 0)) {
    mq -> no_readers = true;
  }
  if ((flags & MSG_QUEUE_WRITER) && (--mq -> writers == 0)) {
    mq -> no_writers = true;
  }
  
  if (--mq -> refs == 0) {
    assert(mq -> readers == 0);
    assert(mq -> writers == 0);
    return true;
  }
  return false;
}

msg_queue_t msg_queue_create(size_t capacity, int flags) {
  if (flags & ~ALL_FLAGS) {
    errno = EINVAL;
    report_error("msg_queue_create");
    return MSG_QUEUE_NULL;
  }
  
  mq_backend * mq = (mq_backend * ) malloc(sizeof(mq_backend));
  if (!mq) {
    report_error("malloc");
    return MSG_QUEUE_NULL;
  }
  // Result of malloc() is always aligned on 8 bytes, allowing us to use the
  // 3 least significant bits of the handle to store the 3 bits of flags
  assert(((uintptr_t) mq & ALL_FLAGS) == 0);
  
  if (mq_init(mq, capacity) < 0) {
    // Preserve errno value that can be changed by free()
    int e = errno;
    free(mq);
    errno = e;
    return MSG_QUEUE_NULL;
  }
  
  return mq_open(mq, flags); //mq_open essentially make handle and update backend attributes
}

msg_queue_t msg_queue_open(msg_queue_t queue, int flags) {
  if (!queue) {
    errno = EBADF;
    report_error("msg_queue_open");
    return MSG_QUEUE_NULL;
  }
  
  if (flags & ~ALL_FLAGS) {
    errno = EINVAL;
    report_error("msg_queue_open");
    return MSG_QUEUE_NULL;
  }
  
  mq_backend * mq = get_backend(queue);
  
  //TODO: add necessary synchronization
  
  // try to get lock from backend
  mutex_lock( & mq -> mutex);
  msg_queue_t new_handle = mq_open(mq, flags); //mq_open essentially make handle and update backend attributes
  // release the lock
  mutex_unlock( & mq -> mutex);
  
  return new_handle;
}

/**
 * Close a message queue handle and invalidate it (set to MSG_QUEUE_NULL).
 *
 * The queue is destroyed when the last handle is closed. If this is the last
 * reader (or writer) handle (but not the very last handle), must notify all the
 * writer (or reader) threads currently blocked in msg_queue_write() (or
 * msg_queue_read()) and msg_queue_poll() calls for this queue.
 *
 * Errors:
 *   EBADF   queue is not a pointer to a valid message queue handle.
 *
 * @param queue  pointer to the message queue handle.
 * @return       0 on success; -1 on failure (with errno set).
 */
int msg_queue_close(msg_queue_t * queue) {
  if (!queue || ! * queue) {
    errno = EBADF;
    report_error("msg_queue_close");
    return -1;
  }
  
  mq_backend * mq = get_backend( * queue);
  
  //TODO: add necessary synchronization
  mutex_lock( & mq -> mutex);
  if (mq_close(mq, get_flags( * queue))) {
    mutex_unlock( & mq -> mutex);
    // Closed last handle; destroy the queue
    mq_destroy(mq);
    free(mq);
    * queue = MSG_QUEUE_NULL;
    return 0;
  }
  
  //TODO: if this is the last reader (or writer) handle, notify all the writer
  // (or reader) threads currently blocked in msg_queue_write() (or
  // msg_queue_read()) and msg_queue_poll() calls for this queue.
  
  struct list_entry * cur_entry;
  
  if (mq -> no_readers || mq -> no_writers) {
    //notify blocked writers or blocked readers
    if (get_flags( * queue) & MSG_QUEUE_READER) {
      cond_broadcast( & (mq -> cond_write));
    } else if (get_flags( * queue) & MSG_QUEUE_WRITER) {
      cond_broadcast( & (mq -> cond_read));
    }
    //notify poll
    list_for_each(cur_entry, mq -> linked_list) {
      fd_poll_wrapper * cur_fd_poll_wrapper = container_of(cur_entry, fd_poll_wrapper, entry);
      if (cur_fd_poll_wrapper -> request_event & (MQPOLL_NOREADERS | MQPOLL_NOWRITERS)) {
        mutex_lock(cur_fd_poll_wrapper -> mutex);
        
        * cur_fd_poll_wrapper -> signal = true;
        cond_signal(cur_fd_poll_wrapper -> cond);
        
        mutex_unlock(cur_fd_poll_wrapper -> mutex);
      }
    }
  }
  * queue = MSG_QUEUE_NULL;
  mutex_unlock( & mq -> mutex);
  
  return 0;
}

ssize_t msg_queue_read(msg_queue_t queue, void * buffer, size_t length) {
  //fprintf(stderr, "enter read\n");
  //TODO
  mq_backend * backend = get_backend(queue);
  mutex_lock( & (backend -> mutex));
  
  // return error if there is no flag for reader
  if (!(get_flags(queue) & MSG_QUEUE_READER)) {
    errno = EBADF;
    report_error("msg_queue_read: the flag does not include reader.");
    mutex_unlock( & (backend -> mutex));
    return -1;
  }
  
  // if non-block mode, no data to read return EAGAIN
  if ((get_flags(queue) & MSG_QUEUE_NONBLOCK) && (ring_buffer_used( & (backend -> buffer)) == 0)) {
    errno = EAGAIN;
    report_error("msg_queue_read: no data and non-block.");
    return -1;
  }
  
  //if the buffer is empty, then we wait for read except for no writer ever created yet
  while (ring_buffer_used( & (backend -> buffer)) == 0) {
    // if there is no writers, then we return
    if (backend -> no_writers && backend -> writer_existed) {
      assert(ring_buffer_used( & (backend -> buffer)) == 0);
      mutex_unlock( & (backend -> mutex));
      return 0;
    }
    cond_wait( & (backend -> cond_read), & (backend -> mutex));
  }
  
  size_t message_size;
  ring_buffer_peek( & (backend -> buffer), & message_size, sizeof(size_t));
  
  // if the message_size is larger than buffer
  if (message_size > length) {
    errno = EMSGSIZE;
    mutex_unlock( & (backend -> mutex));
    report_error("msg_queue_read: the message_size is larger than buffer");
    return -message_size;
  }
  
   
  ring_buffer_read( & (backend -> buffer), & message_size, sizeof(size_t));
 
  ring_buffer_read( & (backend -> buffer), buffer, message_size);
  
  //signal conditional variable
  cond_signal( & (backend -> cond_write));
  
  struct list_entry * cur_entry = NULL;
  list_for_each(cur_entry, backend -> linked_list) {
    fd_poll_wrapper * cur_fd_poll_wrapper = container_of(cur_entry,
                                                         fd_poll_wrapper, entry);
    if (cur_fd_poll_wrapper -> request_event & MQPOLL_WRITABLE) {
      mutex_lock(cur_fd_poll_wrapper -> mutex);
      * cur_fd_poll_wrapper -> signal = true;
      cond_signal(cur_fd_poll_wrapper -> cond);
      mutex_unlock(cur_fd_poll_wrapper -> mutex);
    }
  }
  mutex_unlock( & backend -> mutex);
  return message_size;
}

int msg_queue_write(msg_queue_t queue,
                    const void * buffer, size_t length) {
  //TODO
  mq_backend * backend = get_backend(queue);
  mutex_lock( & (backend -> mutex));
  
  if (!(get_flags(queue) & MSG_QUEUE_WRITER)) {
    errno = EBADF;
    mutex_unlock( & (backend -> mutex));
    report_error("msg_queue_write: queue is not a valid message queue handle open for writes.");
    return -1;
  }
  
  if (length == 0) {
    errno = EINVAL;
    mutex_unlock( & (backend -> mutex));
    report_error("msg_queue_write: Zero length message.");
    return -1;
  }
  
  // if the length is greater than the buffer's size
  if ((length + sizeof(size_t)) > backend -> buffer.size) {
    errno = EMSGSIZE;
    mutex_unlock( & (backend -> mutex));
    report_error("msg_queue_write: The queue buffer is not large enough to hold the message.");
    return -1;
  }
  
  if ((get_flags(queue) & MSG_QUEUE_NONBLOCK) && (length + sizeof(size_t) > ring_buffer_free( & (backend -> buffer)))) {
    errno = EAGAIN;
    report_error("msg_queue_write: The queue handle is non-blocking and the write would block.");
    mutex_unlock( & (backend -> mutex));
    return -1;
  }
  
  if (backend -> no_readers && backend -> reader_existed) {
    errno = EPIPE;
    report_error("msg_queue_write: All reader handles to the queue have been closed.");
    mutex_unlock( & (backend -> mutex));
    return -1;
  }
  
  while (ring_buffer_free( & (backend -> buffer)) < (length + sizeof(size_t))) {
    // if there is no reader, then we return
    if (backend -> no_readers && backend -> reader_existed) {
      errno = EPIPE;
      report_error("msg_queue_write: All reader handles to the queue have been closed.");
      mutex_unlock( & (backend -> mutex));
      return -1;
    }
    cond_wait( & (backend -> cond_write), & (backend -> mutex));
  }
  
  //write the message size
 
  ring_buffer_write( & (backend -> buffer), & length, sizeof(size_t));
  
  
  //write the message contents
  ring_buffer_write( & (backend -> buffer), buffer, length);
  
  
  cond_signal( & (backend -> cond_read));
  struct list_entry * cur_entry = NULL;
  
  //notify poll
  list_for_each(cur_entry, backend -> linked_list) {
    fd_poll_wrapper * cur_fd_poll_wrapper = container_of(cur_entry,
                                                         fd_poll_wrapper, entry);
    if (cur_fd_poll_wrapper -> request_event & MQPOLL_READABLE) {
      mutex_lock(cur_fd_poll_wrapper -> mutex);
      
      * cur_fd_poll_wrapper -> signal = true;
      cond_signal(cur_fd_poll_wrapper -> cond);
      
      mutex_unlock(cur_fd_poll_wrapper -> mutex);
    }
  }
  mutex_unlock( & backend -> mutex);
  return 0;
}

int msg_queue_poll(msg_queue_pollfd * fds, size_t nfds) {
  //TODO
  if (nfds == 0) {
    errno = EINVAL;
    report_error("nfds is 0");
    return -1;
  }
  
  // Error Checking
  size_t nullQ_count = 0;
  for (size_t i = 0; i < nfds; i++) {
    if (fds[i].queue == MSG_QUEUE_NULL) {
      nullQ_count++;
      continue;
    }
    
    if (fds[i].queue != MSG_QUEUE_NULL) {
      // CHECK: Valid events
      if (!(fds[i].events & ALL_EVENT_FLAGS)) {
        errno = EINVAL;
        return -1;
      }
      /// CHECK: Valid combination of event and handle
      if ((fds[i].events & MQPOLL_READABLE) && (!(get_flags(fds[i].queue) & MSG_QUEUE_READER))) {
        errno = EINVAL;
        return -1;
      }
      if ((fds[i].events & MQPOLL_WRITABLE) && (!(get_flags(fds[i].queue) & MSG_QUEUE_WRITER))) {
        errno = EINVAL;
        return -1;
      }
    }
  }
  // All queues are MSG_QUEUE_NULL
  if (nullQ_count == nfds) {
    errno = EINVAL;
    return -1;
  }
  
  // Initialize the lock, cond, and signal
  mutex_t mutex;
  cond_t cond;
  bool signal;
  mutex_init( & mutex);
  cond_init( & cond);
  signal = false;
  int ready = 0;
  fd_poll_wrapper * fd_wrappers[nfds];
  
  // Initialization: fill all fd wrappers
  for (size_t i = 0; i < nfds; i++) {
    if (fds[i].queue != MSG_QUEUE_NULL) {
      fd_wrappers[i] = malloc(sizeof(fd_poll_wrapper));
      if (fd_wrappers[i] == NULL) {
        errno = ENOMEM;
        cond_destroy( & cond);
        mutex_destroy( & mutex);
        report_error("msg_queue_poll: Not enough memory");
        return -1;
      }
      fd_wrappers[i] -> cond = & cond;
      fd_wrappers[i] -> mutex = & mutex;
      fd_wrappers[i] -> request_event = fds[i].events;
      fd_wrappers[i] -> signal = & signal;
      list_entry_init( & fd_wrappers[i] -> entry);
    }
  }
  
  // do the first time check events
  for (size_t i = 0; i < nfds; ++i) {
    if (!fds[i].queue) {
      fds[i].revents = 0;
      continue;
    }
    mq_backend * backend = get_backend(fds[i].queue);
    int event = fds[i].events;
    int flags = get_flags(fds[i].queue);
    (void)flags;
    mutex_lock( & backend -> mutex);
    fds[i].revents = 0;
    
    if (event == (MQPOLL_NOREADERS | MQPOLL_NOWRITERS)) {
        if (backend -> no_readers && backend->no_writers) {
          fds[i].revents = MQPOLL_NOREADERS | MQPOLL_NOWRITERS;
          ready++;
          if (list_entry_is_linked( & fd_wrappers[i] -> entry)) {
            list_del(backend -> linked_list, & fd_wrappers[i] -> entry);
          }     
        }
      }

    if (event == MQPOLL_NOREADERS) {
        if (backend -> no_readers) {
          fds[i].revents |= MQPOLL_NOREADERS;
          ready++;
          if (list_entry_is_linked( & fd_wrappers[i] -> entry)) {
            list_del(backend -> linked_list, & fd_wrappers[i] -> entry);
          }
        }
      }

    if (event == MQPOLL_NOWRITERS) {
      if (backend -> no_writers) {
        fds[i].revents |= MQPOLL_NOWRITERS;
        ready++;
        if (list_entry_is_linked( & fd_wrappers[i] -> entry)) {
          list_del(backend -> linked_list, & fd_wrappers[i] -> entry);
        }
      }
    }

    if (event & MQPOLL_WRITABLE) {
      assert(flags & MSG_QUEUE_WRITER);
      if (!backend -> buffer.full || backend -> no_readers) {
        fds[i].revents |= MQPOLL_WRITABLE;
        if (backend -> no_readers) {
          fds[i].revents |= MQPOLL_NOREADERS;
        }
        ready++;
        mutex_unlock( & backend -> mutex);
        continue;
      }
    }
    
    if (event & MQPOLL_READABLE) {
      assert(flags & MSG_QUEUE_READER);
      if (!(ring_buffer_used( & (backend -> buffer)) == 0) || backend -> no_writers) {
        fds[i].revents |= MQPOLL_READABLE;
        if (backend -> no_writers) {
          fds[i].revents |= MQPOLL_NOWRITERS;
        }
        ready++;
        mutex_unlock( & backend -> mutex);
        continue;
      }
    }
    
    list_add_head(backend -> linked_list, & fd_wrappers[i] -> entry);
    mutex_unlock( & backend -> mutex);
  }
  
  while (ready == 0) {
    mutex_lock( & mutex);
    while (!signal) {
      cond_wait( & cond, & mutex);
    }
    mutex_unlock( & mutex);
    
    for (size_t i = 0; i < nfds; ++i) {
      if (!fds[i].queue) {
        fds[i].revents = 0;
        continue;
      }
      mq_backend * backend = get_backend(fds[i].queue);
      int event = fds[i].events;
      int flags = get_flags(fds[i].queue);
      (void)flags;
      mutex_lock( & backend -> mutex);
      fds[i].revents = 0;

      if (event == (MQPOLL_NOREADERS | MQPOLL_NOWRITERS)) {
        if (backend -> no_readers && backend->no_writers) {
          fds[i].revents = MQPOLL_NOREADERS | MQPOLL_NOWRITERS;
          ready++;
          if (list_entry_is_linked( & fd_wrappers[i] -> entry)) {
            list_del(backend -> linked_list, & fd_wrappers[i] -> entry);
          }     
        }
      }

      if (event == MQPOLL_NOREADERS) {
        if (backend -> no_readers) {
          fds[i].revents |= MQPOLL_NOREADERS;
          ready++;
          if (list_entry_is_linked( & fd_wrappers[i] -> entry)) {
            list_del(backend -> linked_list, & fd_wrappers[i] -> entry);
          }     
        }
      }

      if (event == MQPOLL_NOWRITERS) {
        if (backend -> no_writers) {
          fds[i].revents |= MQPOLL_NOWRITERS;
          ready++;
          if (list_entry_is_linked( & fd_wrappers[i] -> entry)) {
            list_del(backend -> linked_list, & fd_wrappers[i] -> entry);
          }
        }
      }


      if (event & MQPOLL_WRITABLE) {
        assert(flags & MSG_QUEUE_WRITER);
        if (!backend -> buffer.full || backend -> no_readers) {
          fds[i].revents |= MQPOLL_WRITABLE;
          if (backend -> no_readers) {
            fds[i].revents |= MQPOLL_NOREADERS;
          }
          ready++;
          if (list_entry_is_linked( & fd_wrappers[i] -> entry)) {
            list_del(backend -> linked_list, & fd_wrappers[i] -> entry);
          }
          mutex_unlock( & backend -> mutex);
          continue;
        }
      }
      
      if (event & MQPOLL_READABLE) {
        assert(flags & MSG_QUEUE_READER);
        if (!(ring_buffer_used( & (backend -> buffer)) == 0) || backend -> no_writers) {
          fds[i].revents |= MQPOLL_READABLE;
          if (backend -> no_writers) {
            fds[i].revents |= MQPOLL_NOWRITERS;
          }
          ready++;
          if (list_entry_is_linked( & fd_wrappers[i] -> entry)) {
            list_del(backend -> linked_list, & fd_wrappers[i] -> entry);
          }
          mutex_unlock( & backend -> mutex);
          continue;
        }
      }
      
      if (!list_entry_is_linked( & fd_wrappers[i] -> entry)) {
        list_add_head(backend -> linked_list, & fd_wrappers[i] -> entry);
      }
      mutex_unlock( & backend -> mutex);
    }
    signal = false;
    
  }
  
  for (size_t i = 0; i < nfds; ++i) {
    if (!fds[i].queue) {
      continue;
    }
    mq_backend * mq = get_backend(fds[i].queue);
    mutex_lock( & mq -> mutex);
    if (list_entry_is_linked( & fd_wrappers[i] -> entry)) {
      list_del(mq -> linked_list, & fd_wrappers[i] -> entry);
    }
    mutex_unlock( & mq -> mutex);
    free(fd_wrappers[i]);
  }
  
  cond_destroy( & cond);
  mutex_destroy( & mutex);
  
  return ready;
}
