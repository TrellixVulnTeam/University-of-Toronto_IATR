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
 * CSC369 Assignment 1 - File system runtime context header file.
 */

#pragma once

#include <stddef.h>

#include "options.h"


/**
 * Mounted file system runtime state - "fs context".
 */
typedef struct fs_ctx {
	/** Pointer to the start of the image. */
	void *image;
	/** Image size in bytes. */
	size_t size;

	//TODO: useful runtime state of the mounted file system should be cached
	// here (NOT in global variables in a1fs.c)

	// pointer for super block
	struct a1fs_superblock* super_block;

	// pointer for inode bitmap
	unsigned char* inode_bitmap_address;

	// pointer for block bitmap
	unsigned char* block_bitmap_address;

	// pointer for inode table
	unsigned char* inode_table_address;

	// pointer for real data blocks starting point
	unsigned char* real_data_blocks_sp;

	//how many inodes are used currently
	// unsigned int curr_inodes_count; 

} fs_ctx;

/**
 * Initialize file system context.
 *
 * @param fs     pointer to the context to initialize.
 * @param image  pointer to the start of the image.
 * @param size   image size in bytes.
 * @return       true on success; false on failure (e.g. invalid superblock).
 */
bool fs_ctx_init(fs_ctx *fs, void *image, size_t size);

/**
 * Destroy file system context.
 *
 * Must cleanup all the resources created in fs_ctx_init().
 */
void fs_ctx_destroy(fs_ctx *fs);
