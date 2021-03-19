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
 * CSC369 Assignment 1 - File system runtime context implementation.
 */

#include "fs_ctx.h"
#include "a1fs.h"

bool fs_ctx_init(fs_ctx *fs, void *image, size_t size)
{
	fs->image = image;
	fs->size = size;

	//TODO: check if the file system image can be mounted and initialize its
	// runtime state

	//extract the super block from image address
	struct a1fs_superblock* super_block = (struct a1fs_superblock*)image;

	//check if input image is a1fs image
	if (super_block->magic != A1FS_MAGIC){
		return false;
	}

	fs->super_block = super_block;

	// pointer for inode bitmap
	fs->inode_bitmap_address = (unsigned char*)(image + super_block->inode_bitmap * A1FS_BLOCK_SIZE);

	// pointer for block bitmap
	fs->block_bitmap_address = (unsigned char*)(image + super_block->block_bitmap * A1FS_BLOCK_SIZE);

	// pointer for inode table
	fs->inode_table_address = (unsigned char*)(image + super_block->inode_table * A1FS_BLOCK_SIZE);

	// pointer for real data blocks starting point
	fs->real_data_blocks_sp = (unsigned char*)(image + super_block->data_blocks_str * A1FS_BLOCK_SIZE);

	// calculate current active/used inode count
	//fs->curr_inodes_count = super_block->inodes_count - super_block->free_inodes_count;

	return true;
}

void fs_ctx_destroy(fs_ctx *fs)
{
	//TODO: cleanup any resources allocated in fs_ctx_init()
	fs->image=NULL;
	fs->size = 0;
	fs->super_block = NULL;

	fs->inode_bitmap_address = NULL;
	fs->block_bitmap_address = NULL;
	fs->inode_table_address = NULL;
	fs->real_data_blocks_sp = NULL;
}
