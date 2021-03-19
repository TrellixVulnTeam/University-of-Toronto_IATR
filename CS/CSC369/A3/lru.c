/*
 * This code is provided solely for the personal and private use of students
 * taking the CSC369H course at the University of Toronto. Copying for purposes
 * other than this use is expressly prohibited. All forms of distribution of
 * this code, including but not limited to public repositories on GitHub,
 * GitLab, Bitbucket, or any other online platform, whether as given or with
 * any changes, are expressly prohibited.
 *
 * Authors: Andrew Peterson, Karen Reid
 *
 * All of the files in this directory and all subdirectories are:
 * Copyright (c) 2019, 2020 Karen Reid
 */

#include "pagetable.h"
#include "sim.h"

unsigned total_count;

/* Page to evict is chosen using the accurate LRU algorithm.
 * Returns the page frame number (which is also the index in the coremap)
 * for the page that is to be evicted.
 */
int lru_evict(void)
{
	//TODO
	unsigned int i;
	unsigned int res_index = 0;
	unsigned int res = coremap[0].lru_count;

	for (i = 0; i < memsize; i++){
		if (coremap[i].lru_count < res){
			res_index = i;
			res = coremap[i].lru_count;
		}	
	}

	return res_index;
}

/* This function is called on each access to a page to update any information
 * needed by the LRU algorithm.
 * Input: The page table entry for the page that is being accessed.
 */
void lru_ref(pgtbl_entry_t *p)
{
	//(void)p;
	//TODO
	int frame_num = p->frame >> PAGE_SHIFT;
	total_count++;
	coremap[frame_num].lru_count = total_count;

}

/* Initialize any data structures needed for this replacement algorithm. */
void lru_init(void)
{
	//TODO
	total_count = 0;
	unsigned int i;
	for (i = 0; i < memsize; i++){
		coremap[i].lru_count = 0;
	}
}

/* Cleanup any data structures created in lru_init(). */
void lru_cleanup(void)
{
	//TODO
	total_count = 0;
	unsigned int i;
	for (i = 0; i < memsize; i++){
		coremap[i].lru_count = 0;
	}
}
