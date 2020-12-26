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
 * Copyright (c) 2020 Karen Reid
 */
#include <assert.h>
#include <string.h> 
#include "sim.h"
#include "pagetable.h"

// The top-level page table (also known as the 'page directory')
pgdir_entry_t pgdir[PTRS_PER_PGDIR]; 

// Counters for various events.
// Your code must increment these when the related events occur.
int hit_count = 0;
int miss_count = 0;
int ref_count = 0;
int evict_clean_count = 0;
int evict_dirty_count = 0;

/*
 * Allocates a frame to be used for the virtual page represented by p.
 * If all frames are in use, calls the replacement algorithm's evict_fcn to
 * select a victim frame.  Writes victim to swap if needed, and updates 
 * pagetable entry for victim to indicate that virtual page is no longer in
 * (simulated) physical memory.
 *
 * Counters for evictions should be updated appropriately in this function.
 */
static int allocate_frame(pgtbl_entry_t *p)
{
	int frame = -1;
	for (unsigned i = 0; i < memsize; i++) {
		if (!coremap[i].in_use) {
			frame = i;
			break;
		}
	}

	if (frame == -1) { // Didn't find a free page.
		// Call replacement algorithm's evict function to select victim
		frame = evict_fcn();

		// All frames were in use, so victim frame must hold some page
		// Write victim page to swap, if needed, and update pagetable
		// IMPLEMENTATION NEEDED
		pgtbl_entry_t *victim_pte = coremap[frame].pte;

		// swapout if dirty
		if (victim_pte->frame & PG_DIRTY){
			
			//swap
			int swap_offset = swap_pageout(frame, victim_pte->swap_off);
			if (swap_offset == INVALID_SWAP){
				return -1;
			}
			victim_pte->swap_off = swap_offset;
			victim_pte->frame |= PG_ONSWAP;
			// update dirty count
			evict_dirty_count ++;
		}
		else
		{
			evict_clean_count ++;
		}
		// Then, shift
		// int shifted_frame = victim_pte->frame >> PAGE_SHIFT;

		// update status bits
		victim_pte->frame &= ~PG_VALID;
		victim_pte->frame &= ~PG_DIRTY;
		
	}

	// Record information for virtual page that will now be stored in frame
	coremap[frame].in_use = 1;
	coremap[frame].pte = p;

	return frame;
}

/*
 * Initializes the top-level pagetable.
 * This function is called once at the start of the simulation.
 * For the simulation, there is a single "process" whose reference trace is 
 * being simulated, so there is just one top-level page table (page directory).
 * To keep things simple, we use a global array of 'page directory entries'.
 *
 * In a real OS, each process would have its own page directory, which would
 * need to be allocated and initialized as part of process creation.
 */
void init_pagetable(void)
{
	// Set all entries in top-level pagetable to 0, which ensures valid
	// bits are all 0 initially.
	for (int i = 0; i < PTRS_PER_PGDIR; i++) {
		pgdir[i].pde = 0;
	}
}

// For simulation, we get second-level pagetables from ordinary memory
static pgdir_entry_t init_second_level(void)
{
	pgtbl_entry_t *pgtbl;
	// Allocating aligned memory ensures the low bits in the pointer must
	// be zero, so we can use them to store our status bits, like PG_VALID
	if (posix_memalign((void **)&pgtbl, PAGE_SIZE,
	                   PTRS_PER_PGTBL * sizeof(pgtbl_entry_t)) != 0) {
		perror("Failed to allocate aligned memory for page table");
		exit(1);
	}

	// Initialize all entries in second-level pagetable
	for (int i = 0; i < PTRS_PER_PGTBL; i++) {
		pgtbl[i].frame = 0; // sets all bits, including valid, to zero
		pgtbl[i].swap_off = INVALID_SWAP;
	}

	pgdir_entry_t new_entry;
	// Mark the new page directory entry as valid
	new_entry.pde = (uintptr_t)pgtbl | PG_VALID;

	return new_entry;
}

/* 
 * Initializes the content of a (simulated) physical memory frame when it 
 * is first allocated for some virtual address.  Just like in a real OS,
 * we fill the frame with zero's to prevent leaking information across
 * pages. 
 * 
 * In our simulation, we also store the the virtual address itself in the 
 * page frame to help with error checking.
 *
 */
static void init_frame(int frame, addr_t vaddr)
{
	// Calculate pointer to start of frame in (simulated) physical memory
	char *mem_ptr = &physmem[frame * SIMPAGESIZE];
	// Calculate pointer to location in page where we keep the vaddr
	addr_t *vaddr_ptr = (addr_t *)(mem_ptr + sizeof(int));

	memset(mem_ptr, 0, SIMPAGESIZE); // zero-fill the frame
	*vaddr_ptr = vaddr;              // record the vaddr for error checking
}

/*
 * Locate the physical frame number for the given vaddr using the page table.
 *
 * If the entry is invalid and not on swap, then this is the first reference 
 * to the page and a (simulated) physical frame should be allocated and 
 * initialized (using init_frame).  
 *
 * If the entry is invalid and on swap, then a (simulated) physical frame
 * should be allocated and filled by reading the page data from swap.
 *
 * Counters for hit, miss and reference events should be incremented in
 * this function.
 */
char *find_physpage(addr_t vaddr, char type)
{
	pgtbl_entry_t *p = NULL; // pointer to the full page table entry for vaddr
	unsigned idx = PGDIR_INDEX(vaddr); // get index into page directory

	// To keep compiler happy - remove when you have a real use.
	// (void)idx;
	// (void)type;
	// (void)allocate_frame;
	// (void)init_second_level;
	// (void)init_frame;

	// IMPLEMENTATION NEEDED
	// Use top-level page directory to get pointer to 2nd-level page table
	pgdir_entry_t master_entry_ptr = pgdir[idx];
	if ((master_entry_ptr.pde & PG_VALID) == 0){
		pgdir[idx] = init_second_level();
	}

	// Use vaddr to get index into 2nd-level page table and initialize 'p'
	unsigned sec_idx = PGTBL_INDEX(vaddr); // get index into second page frame
	pgtbl_entry_t * pgtbl_e_ptr = (pgtbl_entry_t *)(pgdir[idx].pde & PAGE_MASK);
	p = &pgtbl_e_ptr[sec_idx];

	// Check if p is valid or not, on swap or not, and handle appropriately
	// (Note that the first acess to a page will be marked DIRTY.)
	if (p->frame & PG_VALID){
		hit_count ++;
	}
	else{
		int frame = allocate_frame(p);

		if(p->frame & PG_ONSWAP){
			int res = swap_pagein(frame, p->swap_off);
			if (res != 0){
				perror("swap_pagein failed");
				exit(-1);
			}
			p->frame = frame << PAGE_SHIFT;
			p->frame &= ~PG_DIRTY;
            p->frame |=  PG_ONSWAP;
            
		}
		else{
			init_frame(frame, vaddr);
			p->frame = frame << PAGE_SHIFT;
			p->frame |= PG_DIRTY;
            p->frame |=  PG_ONSWAP;
            
		}
		miss_count ++;
	}


	// Make sure that p is marked valid and referenced. Also mark it
	// dirty if the access type indicates that the page will be written to.
	p->frame |= (PG_VALID | PG_REF);

	ref_count ++;

	if (type == 'S' || type == 'M'){
		p->frame |= PG_DIRTY;
	}


	// Call replacement algorithm's ref_fcn for this page
	ref_fcn(p);

	// Return pointer into (simulated) physical memory at start of frame
	return &physmem[(p->frame >> PAGE_SHIFT) * SIMPAGESIZE];
}

void print_pagetable(pgtbl_entry_t *pgtbl)
{
	int first_invalid = -1, last_invalid = -1;

	for (int i = 0; i < PTRS_PER_PGTBL; i++) {
		if (!(pgtbl[i].frame & PG_VALID) && !(pgtbl[i].frame & PG_ONSWAP)) {
			if (first_invalid == -1) {
				first_invalid = i;
			}
			last_invalid = i;
		} else {
			if (first_invalid != -1) {
				printf("\t[%d] - [%d]: INVALID\n",
				       first_invalid, last_invalid);
				first_invalid = last_invalid = -1;
			}
			printf("\t[%d]: ", i);
			if (pgtbl[i].frame & PG_VALID) {
				printf("VALID, ");
				if (pgtbl[i].frame & PG_DIRTY) {
					printf("DIRTY, ");
				}
				printf("in frame %d\n", pgtbl[i].frame >> PAGE_SHIFT);
			} else {
				assert(pgtbl[i].frame & PG_ONSWAP);
				printf("ONSWAP, at offset %lu\n", (unsigned long)pgtbl[i].swap_off);
			}			
		}
	}
	if (first_invalid != -1) {
		printf("\t[%d] - [%d]: INVALID\n", first_invalid, last_invalid);
		first_invalid = last_invalid = -1;
	}
}

void print_pagedirectory(void)
{
	int first_invalid = -1, last_invalid = -1;

	for (int i = 0; i < PTRS_PER_PGDIR; i++) {
		if (!(pgdir[i].pde & PG_VALID)) {
			if (first_invalid == -1) {
				first_invalid = i;
			}
			last_invalid = i;
		} else {
			if (first_invalid != -1) {
				printf("[%d]: INVALID\n  to\n[%d]: INVALID\n", 
				       first_invalid, last_invalid);
				first_invalid = last_invalid = -1;
			}
			pgtbl_entry_t *pgtbl = (pgtbl_entry_t *)(pgdir[i].pde & PAGE_MASK);
			printf("[%d]: %p\n", i, pgtbl);
			print_pagetable(pgtbl);
		}
	}
}
