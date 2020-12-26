/*
 * This code is provided solely for the personal and private use of students
 * taking the CSC369H course at the University of Toronto. Copying for purposes
 * other than this use is expressly prohibited. All forms of distribution of
 * this code, including but not limited to public repositories on GitHub,
 * GitLab, Bitbucket, or any other online platform, whether as given or with
 * any changes, are expressly prohibited.
 *
 * Authors: Alexey Khrabrov, Karen Reid
 *
 * All of the files in this directory and all subdirectories are:
 * Copyright (c) 2020 Karen Reid
 */

/**
 * CSC369 Assignment 1 - Miscellaneous utility functions.
 */

#pragma once

#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include "a1fs.h"
#include "fs_ctx.h"

/** Check if x is a power of 2. */
static inline bool is_powerof2(size_t x)
{
	return (x & (x - 1)) == 0;
}

/** Check if x is a multiple of alignment (which must be a power of 2). */
static inline bool is_aligned(size_t x, size_t alignment)
{
	assert(is_powerof2(alignment));
	return (x & (alignment - 1)) == 0;
}

/** Align x up to a multiple of alignment (which must be a power of 2). */
static inline size_t align_up(size_t x, size_t alignment)
{
	assert(is_powerof2(alignment));
	return (x + alignment - 1) & (~alignment + 1);
}

static inline void print_bitmap(unsigned char* b, int end)
{
  int num_of_byte;
  int in_use_bit;
  int bit, byte;
  num_of_byte = end / 8;

  for (byte = 0; byte < num_of_byte; byte++) {
    for (bit = 0; bit < 8; bit++) {
		in_use_bit = b[byte] & (1 << bit);
      	if(in_use_bit >= 1){
				fprintf(stderr, "1");
      	}
		else{
        fprintf(stderr, "0");
      	}
    }

    if (byte != (num_of_byte - 1)) {
      fprintf(stderr, " ");
    }
  }
  fprintf(stderr, "\n");

}


//based on inode table and inodeID number, return the inode struct
//otherwise return NULL
static inline void getInodeByID(fs_ctx *fs, int inodeID, struct a1fs_inode* fileInode){
  fprintf(stderr, "********** enter getInodebyID ************\n");
  unsigned char* inode_bitmap = fs->inode_bitmap_address;
  unsigned char* inode_table = fs->inode_table_address;
  
  int byte = inodeID / 8;
  int bit =   inodeID % 8;
  
  if((inode_bitmap[byte] & (1<<bit)) > 0){ // check inode is in use
    *fileInode = *(struct a1fs_inode*)(inode_table + sizeof(struct a1fs_inode)*inodeID);
  }
  else{
	  fprintf(stderr, "the Inode %d is used\n",inodeID );
	  perror("the Inode %d is used");
  }
  fprintf(stderr, "********** get out from getInodebyID ************\n");
}


/** return empty inode id, If no available inode return -1 */
static inline int get_empty_inode_ID(fs_ctx* fs){
  struct a1fs_superblock* super_block = (struct a1fs_superblock*)fs->image;
  int byte_count = super_block->inodes_count / 8 + (super_block->inodes_count % 8 > 0 ? 1 : 0);
  int count = super_block->inodes_count;
  
  for(int byte = 0; byte < byte_count; byte++){
    for(int bit = 0; bit < 8; bit++){
      int occupied = fs->inode_bitmap_address[byte] & (1<<bit);
      //empty block, can be used
      if ((occupied == 0) && count > 0){
        int empty_inode_id = (byte * 8 + bit);
        return empty_inode_id;
      }
      count--;
    }
  }
  return -1;
}


/*
 * return empty block index if exist. Return -1 otherwise.
 * */
static inline int get_empty_block_index(fs_ctx* fs){
  struct a1fs_superblock* super_block = (struct a1fs_superblock*)fs->image;
  int byte_count = super_block->blocks_count / 8 + (super_block->blocks_count % 8 > 0 ? 1 : 0);
  int count = super_block->blocks_count;
  
  for(int byte = 0; byte < byte_count; byte++){
    for(int bit = 0; bit < 8; bit++){
      int occupied = fs->block_bitmap_address[byte] & (1<<bit);
      //empty block, can be used
      if((occupied == 0) && (count > 0)){
        return (byte * 8 + bit);
      }
      count --;
    }
  }
  return -1;
}

static inline void getParentDirOfPathEnd(fs_ctx *fs, const char *path, struct a1fs_inode* targetInode, char *name){
	fprintf(stderr, "******enter getPartentDirOfPathEnd*******\n");
	char temp_path[A1FS_PATH_MAX];
	strncpy(temp_path, path, strlen(path)+1);
	temp_path[strlen(path)] = '\0';
	
	// /A/B/C/D/E/F/G
	// /A/B
	
	char* curr_name = strtok(temp_path, "/");
	char* next_name = strtok(NULL, "/");
	struct a1fs_inode parent_dir_inode;
	// fprintf(stderr, "******* before getinodebyID *********\n");
	getInodeByID(fs, 0, &parent_dir_inode);
	//   fprintf(stderr, "******* after getinodebyID *********\n");

	//   fprintf(stderr, "check parentInode, inode: %u\n", parent_dir_inode.inode_id);
	//   fprintf(stderr, "check parentInode, entry count: %u\n", parent_dir_inode.entry_count);

	while(next_name != NULL){
		// fprintf(stderr, "******* enter while loop of get parentDir of path End *********\n");
		// Follow path, enter each dir by order
		for(unsigned int i = 0; i < parent_dir_inode.extents_count; i++){
			// fprintf(stderr, "******* !!!!!!!!!!!! *********\n");
			struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + parent_dir_inode.extent_table*A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent)*i);
		for(unsigned int j = 0; j < extent->count * A1FS_BLOCK_SIZE / sizeof(struct a1fs_dentry); j++){
			struct a1fs_dentry* entry = (struct a1fs_dentry*)(fs->image + extent->start*A1FS_BLOCK_SIZE + sizeof(struct a1fs_dentry)*j);
				
			if(strcmp(entry->name, curr_name)==0){ // find curr name entry in parent dir
				///A/B/C/D/E/F/G 极限curr_name == F;entry->name== F, entry is for F.
				
				//update parenet inode
				getInodeByID(fs, entry->ino,&parent_dir_inode); // now enter curr dir
				//fprintf(stderr, "new parent dir inode id %u  \n", parent_dir_inode->inode_id);
						
				curr_name = next_name;
				next_name = strtok(NULL, "/");
				//fprintf(stderr, "update curr parent dir %s file %s \n", curr_name, next_name);
				break;
			}
		}
		if (next_name ==  NULL){
			break;
		}
		}
	}
	//   fprintf(stderr, "******* get out while loop *********\n");

	//   fprintf(stderr, "print cur name: %s\n", curr_name);
	curr_name[strlen(curr_name)] = '\0';
	strncpy(name, curr_name, A1FS_NAME_MAX);

	//   fprintf(stderr, "******* get PDOPE 1  *********\n");
	
	//   fprintf(stderr, "******* get PDOPE 2 *********\n");
	*targetInode = parent_dir_inode;
	//   fprintf(stderr, "**** End getparentInode **********\n");
}



static inline void set_bitmap_by_index(unsigned char* bitmap_address, int index){
	int byte_index = index / 8;
	int bit = index % 8;
	bitmap_address[byte_index] |= 1 << bit;	
}


static inline void reset_bitmap_by_index(unsigned char* bitmap_address, int index){
	int byte_index = index/8;
	int bit = index % 8;
	bitmap_address[byte_index] &= (~(1 << bit));
}

// return 0 if viliad, otherwise 1-ENAMETOOLONG, 2-ENOENT, 3-ENOTDIR
// populate the file inode if valid
static inline int check_path_valid(fs_ctx *fs, const char *path, struct a1fs_inode* file_inode){
	// get cached info from fs struct
	// struct a1fs_superblock* super_block = (struct a1fs_superblock*)fs->image;
	// unsigned char* inode_bitmap_address = fs->inode_bitmap_address;
	// unsigned char* block_bitmap_address = fs->block_bitmap_address;
	// unsigned char* inode_table_address = fs->inode_bitmap_address;

	//check if path is too long
	fprintf(stderr, "enter check path valid, the path is %s \n", path);
	char temp_path[A1FS_PATH_MAX];
	strncpy(temp_path, path, strlen(path)+1);
	temp_path[strlen(path)] = '\0';

	if (strlen(temp_path) > A1FS_PATH_MAX){
		fprintf(stderr, "--------name length exceed limit, get out from check path valid --------\n");
		return 1;
	}

	if(strcmp(temp_path, "/")==0){ // root
		getInodeByID(fs, 0, file_inode);
		fprintf(stderr, "--------path is root, get out from check path valid --------\n");
		return 0;
	}
  
	char* curr_name = strtok(temp_path, "/");
	char* next_name = strtok(NULL, "/");
	//fprintf(stderr,"curr name:%s;   next name:%s\n",curr_name, next_name);
  
  	struct a1fs_inode parent_dir_inode;
	getInodeByID(fs, 0, &parent_dir_inode);
	//fprintf(stderr, "curr parent dir %u \n", parent_dir_inode.inode_id);
	
	int entry_found = -1;
	// Case not root
	while(next_name != NULL){
		for(unsigned int i = 0; i < parent_dir_inode.extents_count; i++){
			struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + parent_dir_inode.extent_table*A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent)*i);
			for(unsigned int j = 0; j < extent->count * A1FS_BLOCK_SIZE / sizeof(struct a1fs_dentry); j++){
				struct a1fs_dentry* entry = (struct a1fs_dentry*)(fs->image + extent->start*A1FS_BLOCK_SIZE + sizeof(struct a1fs_dentry)*j);
				if(strcmp(entry->name, curr_name)==0){ // find curr name entry in parent dir
					if (strlen(entry->name) > A1FS_NAME_MAX){
						fprintf(stderr, "--------one component name length exceed limit, get out from check path valid --------\n");
						return 1;
					}

					//fprintf(stderr, "find entry, check curr parent dir %s file %s \n", curr_name, next_name);
					entry_found = 1;
          
					//update parenet inode
					getInodeByID(fs, entry->ino,&parent_dir_inode); // now enter curr dir
					//fprintf(stderr, "new parent dir inode id %u  \n", parent_dir_inode->inode_id);
					
					// check if curr_name is dir
					if(!(parent_dir_inode.mode & S_IFDIR)){
						//fprintf(stderr, "not dir error \n");
						fprintf(stderr, "--------one component is not dir, get out from check path valid --------\n");
						return 3;
					}

					curr_name = next_name;
					next_name = strtok(NULL, "/");
					//fprintf(stderr, "update curr parent dir %s file %s \n", curr_name, next_name);
					break;
				}
			}	
		}
	
		if(entry_found == -1){
			fprintf(stderr, " \n %s in path doesn't exists \n", curr_name);
			return 2;
		}
	}
  
  	
	// terminate from while, now parent_dir is the last exist dir in the path, curr name is the file in the end of the path
	// fprintf(stderr, "final file %s \n", curr_name);
	entry_found = -1;
  
  	// fprintf(stderr,"The extent count for the parent dir is: %u\n",parent_dir_inode.extents_count);
  	// fprintf(stderr,"curr name:%s;   next name:%s\n",curr_name, next_name);

	for(unsigned int i = 0; i < parent_dir_inode.extents_count; i++){
		struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + parent_dir_inode.extent_table*A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent)*i);
		for(unsigned int j = 0; j < extent->count * A1FS_BLOCK_SIZE / sizeof(struct a1fs_dentry); j++){
			struct a1fs_dentry* entry = (struct a1fs_dentry*)(fs->image + extent->start*A1FS_BLOCK_SIZE + sizeof(struct a1fs_dentry)*j);
			if(strcmp(entry->name, curr_name)==0){ // find curr name entry in parent dir
				if (strlen(entry->name) > A1FS_NAME_MAX){
						fprintf(stderr, "--------file name length exceed limit, get out from check path valid --------\n");
						return 1;
				}
				entry_found = 1;
				getInodeByID(fs, entry->ino, file_inode); // now enter curr dir
				break;
			}
		}	
	}
  	//fprintf(stderr,"The last chance......\n");
	if(entry_found == -1){
		fprintf(stderr, "****Listen %s in path doesn't exists ******\n", curr_name);
		return 2;
	}
	fprintf(stderr, "--------Great, get out from check path valid --------\n");
	return 0;
}

static inline void get_target_inode_from_path(fs_ctx *fs, const char *path, struct a1fs_inode* targetInode){
	fprintf(stderr, "******* enter get target inode from path *********\n");
	char curr_name[A1FS_NAME_MAX];
	struct a1fs_inode parent_dir_inode;
	struct a1fs_inode file_inode;
	
	getParentDirOfPathEnd(fs, path, &parent_dir_inode, curr_name);
	
	
	for(unsigned int i = 0; i < parent_dir_inode.extents_count; i++){
		struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + parent_dir_inode.extent_table*A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent)*i);
		for(unsigned int j = 0; j < extent->count * A1FS_BLOCK_SIZE / sizeof(struct a1fs_dentry); j++){
			struct a1fs_dentry* entry = (struct a1fs_dentry*)(fs->image + extent->start*A1FS_BLOCK_SIZE + sizeof(struct a1fs_dentry)*j);
			if(strcmp(entry->name, curr_name)==0){ // find curr name entry in parent dir
				getInodeByID(fs, entry->ino, &file_inode); 
				break;
			}
		}
	}
	*targetInode = file_inode;
	
}

static inline unsigned int get_the_total_blocks_number(fs_ctx *fs, struct a1fs_inode* inode){
	unsigned counter = 0;
	for(unsigned int i = 0; i < inode->extents_count; i++){
		struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + inode->extent_table * A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent) * i);
		counter += extent->count;
	}
	return counter;
}


static inline void find_longest_consecutive_zeros_dp(fs_ctx* fs, unsigned int* max_block_index, unsigned int* max_cont_length){
	fprintf(stderr, "\t ****************  Enter find longest consecutive zeros dp *****************\n" );
	unsigned char* block_bitmap = fs->block_bitmap_address;
	int block_count = fs->super_block->blocks_count;

	unsigned int dp_array[block_count];
	memset(dp_array, 0, sizeof(int)*block_count);
	
	//base case
	int byte = (block_count-1) / 8;
	int bit = (block_count-1) % 8;
	int if_occupied = block_bitmap[byte] & (1<<bit);

	if (if_occupied == 0){
		dp_array[block_count - 1] = 1;
	}
	block_count--;
	// DP bottom to up while loop
	while (block_count > 0)
	{
		int byte = (block_count-1) / 8;
		int bit = (block_count-1) % 8;
		int if_occupied = block_bitmap[byte] & (1<<bit);
		if (if_occupied == 0){
			dp_array[block_count - 1] = 1 + dp_array[block_count];
		}
		block_count--;
	}
	
	unsigned int max_index = 0;
	unsigned int cur_max = 0;

	for (unsigned int i = 0; i < fs->super_block->blocks_count; i++){
		if (dp_array[i] > cur_max){
			cur_max = dp_array[i];
			max_index = i;
		}
	}
	*max_block_index = max_index;
	*max_cont_length = cur_max;
}



/** find longest continous blocks for data, return 0, if not long enough, return -1 
 * 	whatever the result, populate the three pointer, one for start, one for length, one for new_data_blocks_need
*/
static inline int find_available_longest_blocks(fs_ctx* fs, unsigned int* new_data_blocks_need, unsigned int* start, unsigned int* longest_count){
	fprintf(stderr, "\t ****************  Enter find longest avaliable continuous blocks\n" );
	
	unsigned int max_block_index;
	unsigned int max_cont_length;

	find_longest_consecutive_zeros_dp(fs, &max_block_index, &max_cont_length);

	//populate the two pointers whatever the result
	*start = max_block_index;
	*longest_count = max_cont_length;
	if (max_cont_length >= *new_data_blocks_need){
		fprintf(stderr, "\t *********** Great! Find %d blocks, start from %d th block  ************\n", max_cont_length, max_block_index );
		return 0;
	}
	fprintf(stderr, "\t *********** Find %d blocks, start from %d th block  ************\n", max_cont_length, max_block_index );
	fprintf(stderr, "\t *********** Keep Searching**************************************\n");
	*new_data_blocks_need = *new_data_blocks_need - max_cont_length;
	return -1; // keep search
}
