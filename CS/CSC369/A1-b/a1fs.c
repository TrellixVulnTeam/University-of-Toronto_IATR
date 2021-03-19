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
 * CSC369 Assignment 1 - a1fs driver implementation.
 */

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>

// Using 2.9.x FUSE API
#define FUSE_USE_VERSION 29
#include <fuse.h>

#include "a1fs.h"
#include "fs_ctx.h"
#include "options.h"
#include "map.h"
#include "util.h"


//NOTE: All path arguments are absolute paths within the a1fs file system and
// start with a '/' that corresponds to the a1fs root directory.
//
// For example, if a1fs is mounted at "~/my_csc369_repo/a1b/mnt/", the path to a
// file at "~/my_csc369_repo/a1b/mnt/dir/file" (as seen by the OS) will be
// passed to FUSE callbacks as "/dir/file".
//
// Paths to directories (except for the root directory - "/") do not end in a
// trailing '/'. For example, "~/my_csc369_repo/a1b/mnt/dir/" will be passed to
// FUSE callbacks as "/dir".


/**
 * Initialize the file system.
 *
 * Called when the file system is mounted. NOTE: we are not using the FUSE
 * init() callback since it doesn't support returning errors. This function must
 * be called explicitly before fuse_main().
 *
 * @param fs    file system context to initialize.
 * @param opts  command line options.
 * @return      true on success; false on failure.
 */
static bool a1fs_init(fs_ctx *fs, a1fs_opts *opts)
{
	// Nothing to initialize if only printing help
	if (opts->help) return true;

	size_t size;
	void *image = map_file(opts->img_path, A1FS_BLOCK_SIZE, &size);
	if (!image) return false;

	return fs_ctx_init(fs, image, size);
}

/**
 * Cleanup the file system.
 *
 * Called when the file system is unmounted. Must cleanup all the resources
 * created in a1fs_init().
 */
static void a1fs_destroy(void *ctx)
{
	fs_ctx *fs = (fs_ctx*)ctx;
	if (fs->image) {
		munmap(fs->image, fs->size);
		fs_ctx_destroy(fs);
	}
}

/** Get file system context. */
static fs_ctx *get_fs(void)
{
	return (fs_ctx*)fuse_get_context()->private_data;
}



/**
 * Get file system statistics.
 *
 * Implements the statvfs() system call. See "man 2 statvfs" for details.
 * The f_bfree and f_bavail fields should be set to the same value.
 * The f_ffree and f_favail fields should be set to the same value.
 * The following fields can be ignored: f_fsid, f_flag.
 * All remaining fields are required.
 *
 * Errors: none
 *
 * @param path  path to any file in the file system. Can be ignored.
 * @param st    pointer to the struct statvfs that receives the result.
 * @return      0 on success; -errno on error.
 */
static int a1fs_statfs(const char *path, struct statvfs *st)
{
	(void)path;// unused
	fs_ctx *fs = get_fs();
	fprintf(stderr, " ---------- enter statfs, the path is: %s-------------\n", path);
	memset(st, 0, sizeof(*st));
	st->f_bsize   = A1FS_BLOCK_SIZE;
	st->f_frsize  = A1FS_BLOCK_SIZE;
	//TODO: fill in the rest of required fields based on the information stored
	// in the superblock

	// get super block
	struct a1fs_superblock* super_block = (struct a1fs_superblock*)fs->image;
	
	st->f_blocks = super_block->blocks_count; /* size of fs in f_frsize units */

	st->f_bfree = super_block->free_blocks_count; /* free blocks */
	st->f_bavail = super_block->free_blocks_count; /* free blocks for unprivileged users */

	st->f_files = super_block->inodes_count; /* inodes */

	st->f_ffree = super_block->free_inodes_count; /* free inodes */
	st->f_favail = super_block->free_inodes_count; /* free inodes for unprivileged users */

	st->f_namemax = A1FS_NAME_MAX;

	fprintf(stderr, " ---------- get out from statfs-------------\n");
	return 0;
}

/**
 * Get file or directory attributes.
 *
 * Implements the lstat() system call. See "man 2 lstat" for details.
 * The following fields can be ignored: st_dev, st_ino, st_uid, st_gid, st_rdev,
 *                                      st_blksize, st_atim, st_ctim.
 * All remaining fields are required.
 *
 * NOTE: the st_blocks field is measured in 512-byte units (disk sectors).
 *
 * Errors:
 *   ENAMETOOLONG  the path or one of its components is too long.
 *   ENOENT        a component of the path does not exist.
 *   ENOTDIR       a component of the path prefix is not a directory.
 *
 * @param path  path to a file or directory.
 * @param st    pointer to the struct stat that receives the result.
 * @return      0 on success; -errno on error;
 */
static int a1fs_getattr(const char *path, struct stat *st){
	fprintf(stderr, " ---------- enter getattr, the path is: %s-------------\n", path);

	if (strlen(path) >= A1FS_PATH_MAX) return -ENAMETOOLONG;
	fs_ctx *fs = get_fs();

	
	fprintf(stderr, "print inode bitmap\n");
  	print_bitmap(fs->inode_bitmap_address, fs->super_block->inodes_count);

  	fprintf(stderr, "print block bitmap\n");
  	print_bitmap(fs->block_bitmap_address, fs->super_block->blocks_count);

	memset(st, 0, sizeof(*st));

	//NOTE: This is just a placeholder that allows the file system to be mounted
	// without errors. You should remove this from your implementation.
	
  
	if (strcmp(path, "/") == 0) {
		fprintf(stderr, " ---------- enter root case\n-----------");
		//NOTE: all the fields set below are required and must be set according
		// to the information stored in the corresponding inode
    	struct a1fs_inode root_inode;
		getInodeByID(fs, 0, &root_inode);
		st->st_mode = root_inode.mode;
		st->st_nlink = root_inode.links;
		st->st_size = root_inode.size;
    	st->st_blocks = root_inode.size / 512 + (root_inode.size % 512 > 0 ? 1 : 0);
		st->st_mtim = (struct timespec)root_inode.mtime;
		// fprintf(stderr, "print inode info, inodeID %d\n", root_inode.inode_id);
		// fprintf(stderr, "print inode info, inode link %d\n", root_inode.links);
		fprintf(stderr, " ---------- get out from getattr\n-----------");
		return 0;
	}

	//TODO: lookup the inode for given path and, if it exists, fill in the
	// required fields based on the information stored in the inode


	// check if the path is valid
	// return 0 if valid, getParentDirOfPathEnd
	// otherwise 1-ENAMETOOLONG, 2-ENOENT, 3-ENOTDIR
	struct a1fs_inode file_inode;
	int return_num = check_path_valid(fs, path, &file_inode);

	if (return_num != 0){
		fprintf(stderr, " ---------- something wrong with path, return error is %d\n", return_num);
		if (return_num == 1) return -ENAMETOOLONG;
		else if (return_num == 2) return -ENOENT;
		else if (return_num == 3) return -ENOTDIR;
	}
	// fill the required fields
	st->st_mode = file_inode.mode;
	st->st_nlink = file_inode.links;
	st->st_size = file_inode.size;
  	st->st_blocks = file_inode.size / 512 + (file_inode.size % 512 > 0 ? 1 : 0);
	st->st_mtim = (struct timespec)file_inode.mtime;
	
	fprintf(stderr, " ---------- get from getattr\n-----------");
  return 0;
}

/**
 * Read a directory.
 *
 * Implements the readdir() system call. Should call filler(buf, name, NULL, 0)
 * for each directory entry. See fuse.h in libfuse source code for details.
 *
 * Assumptions (already verified by FUSE using getattr() calls):
 *   "path" exists and is a directory.
 *
 * Errors:
 *   ENOMEM  not enough memory (e.g. a filler() call failed).
 *
 * @param path    path to the directory.
 * @param buf     buffer that receives the result.
 * @param filler  function that needs to be called for each directory entry.
 *                Pass 0 as offset (4th argument). 3rd argument can be NULL.
 * @param offset  unused.
 * @param fi      unused.
 * @return        0 on success; -errno on error.
 */
static int a1fs_readdir(const char *path, void *buf, fuse_fill_dir_t filler,
                        off_t offset, struct fuse_file_info *fi)
{	
	fprintf(stderr, "enter readdir print path %s\n", path);
	(void)offset;// unused
	(void)fi;// unused
	fs_ctx *fs = get_fs();

	//NOTE: This is just a placeholder that allows the file system to be mounted
	// without errors. You should remove this from your implementation.
	// if (strcmp(path, "/") == 0) {
	// 	filler(buf, "." , NULL, 0);
	// 	filler(buf, "..", NULL, 0);
	// 	return 0;
	// }

	//TODO: lookup the directory inode for given path and iterate through its
	// directory entries
	
	//struct a1fs_inode *root_inode = (struct a1fs_inode *)fs->inode_table_address;
	//fprintf(stderr, "***** root inode extents count: %d\n", root_inode->extents_count);
	//fprintf(stderr, "***** root inode entry count: %d\n", root_inode->entry_count);

	
	struct a1fs_inode file_inode;
	int res = check_path_valid(fs, path, &file_inode);
	if (res != 0){
		perror("wrong");
	}
	

	//fprintf(stderr, "***** file inode extents count: %d\n", file_inode.extents_count);
	//fprintf(stderr, "***** file inode entry count: %d\n", file_inode.entry_count);

	int dir_entry_count = file_inode.entry_count;

	// iterate all extents for this inode to read
	for(unsigned int i = 0; i < file_inode.extents_count; i++){
		struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + file_inode.extent_table*A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent)*i);
		if(extent->start != 0){ // check if extent is in use
			int max_possible_entry = (extent->count * A1FS_BLOCK_SIZE) / sizeof(a1fs_dentry);
			// iterate through all entries in parent_dir
			
			for(int j = 0; j < max_possible_entry; j++){
				if(dir_entry_count > 0){
					struct a1fs_dentry* entry = (struct a1fs_dentry*)(fs->image + extent->start*A1FS_BLOCK_SIZE + sizeof(struct a1fs_dentry)*j);
					//fprintf(stderr, "*****write entry name to buffer, entry name: %s **********\n", entry->name);
					if(entry->ino != 0){ // entry is in use
						if(filler(buf, entry->name, NULL, 0) == 1){
							return -ENOMEM;
						}
					dir_entry_count--;
					}
				}
			}
		}
	}
	if (filler(buf, ".", NULL, 0) == 1){
		return -EINVAL;				
	}
	if (filler(buf, "..", NULL, 0) == 1){
		return -EINVAL;				
	}
	fprintf(stderr, "get out from readdir\n");
	return 0;
}


/**
 * Create a directory.
 *
 * Implements the mkdir() system call.
 *
 * Assumptions (already verified by FUSE using getattr() calls):
 *   "path" doesn't exist.
 *   The parent directory of "path" exists and is a directory.
 *   "path" and its components are not too long.
 *
 * Errors:
 *   ENOMEM  not enough memory (e.g. a malloc() call failed).
 *   ENOSPC  not enough free space in the file system.
 *
 * @param path  path to the directory to create.
 * @param mode  file mode bits.
 * @return      0 on success; -errno on error.
 */
static int a1fs_mkdir(const char *path, mode_t mode)
{
	mode = mode | S_IFDIR;
	fs_ctx *fs = get_fs();

	//TODO: create a directory at given path with given mode
	unsigned char* image = fs->image;
	fprintf(stderr, "\n *************  Enter mkdir, the path %s  ************\n", path);
	
	struct a1fs_superblock* super_block = (struct a1fs_superblock*)image;
	unsigned char* block_bitmap = fs->block_bitmap_address;
	unsigned char* inode_bitmap = fs->inode_bitmap_address;
	unsigned char* inode_table = fs->inode_table_address;
	
	// --------- create new inode -----------
	// Write directory entry name
	// Find the inode of the parent dir
	// go to the data block of the parent dir, add new dir entry, (Consider new extent update)
	// Update link, time,
	
	// new inode for new dir
	int new_inode_id = get_empty_inode_ID(fs);
	if(new_inode_id == -1){
		printf("all inodes are in use");
		return -ENOSPC;
	}
	
	// for the inode, find the extent table block
	int new_extent_table_block_num = get_empty_block_index(fs);
	if(new_extent_table_block_num == -1){
		printf("all data block are in use");
		return -ENOSPC;
	}
	//fprintf(stderr, "*****make directory new_extent_table_block_at %u*************************\n", new_extent_table_block_num);
	
	// inode id from 0 to curr_inodes_count are in use, get new inode id
	// update curr_inodes_count by 1 increment
	// if(new_inode_id > fs->curr_inodes_count){
	//   fs->curr_inodes_count++;
	// }
	super_block->free_inodes_count --;
	super_block->free_blocks_count --;
	set_bitmap_by_index(inode_bitmap, new_inode_id);
	set_bitmap_by_index(block_bitmap, new_extent_table_block_num);
	
	// create new inode
	struct a1fs_inode* new_inode = (struct a1fs_inode*)(inode_table + sizeof(struct a1fs_inode)*(new_inode_id));
	new_inode->inode_id = new_inode_id;
	//fprintf(stderr, "new inode is %u\n", new_inode->inode_id);
	
	if((mode | S_IFDIR) != 0){
		new_inode->mode = S_IFDIR;
	};
	
	// if (new_inode->mode == S_IFDIR){
	// 	fprintf(stderr, "mode is directory when mkdir\n");
	// }
	
	new_inode->links = 2;
	new_inode->size = 0; // 0 bytes data contained
	
	if(clock_gettime(CLOCK_REALTIME, &(new_inode->mtime))){
		perror( "clock gettime" );
	};
	
	// unsigned char* data_block_start = fs->real_data_blocks_sp;
	new_inode->extent_table = new_extent_table_block_num;
	new_inode->extents_count = 0;
	new_inode->entry_count = 0;

	// ---------- update parent_dir ------------
	char curr_name[A1FS_NAME_MAX];
	struct a1fs_inode parent_dir_inode;
	
	getParentDirOfPathEnd(fs, path, &parent_dir_inode, curr_name);

	// find extent_table for parent_dir inode
	int extent_table_start = parent_dir_inode.extent_table;
	
	//iterate all extents, find empty one, the maximum number of extents of an inode is 512.
	int updated = -1;
	
	char temp_path[A1FS_PATH_MAX];
	strncpy(temp_path, path, strlen(path)+1);
	temp_path[strlen(path)] = '\0';
	
	
	// fprintf(stderr,"Modify: %ld\n", parent_dir_inode.mtime.tv_sec);
	
	for(unsigned int i = 0; i < parent_dir_inode.extents_count; i++){//loop all extent
		if (updated == -1) {
			struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + extent_table_start * A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent) * i);
			// Loop all directory entry for each inode.
			for(unsigned int j = 0; j < extent->count * A1FS_BLOCK_SIZE / sizeof(struct a1fs_dentry); j++){
				struct a1fs_dentry* new_entry = (struct a1fs_dentry*)(fs->image + extent->start*A1FS_BLOCK_SIZE + sizeof(struct a1fs_dentry)*j);
				if(new_entry->ino == 0){ // empty entry, can be used
					new_entry->ino = new_inode->inode_id;
					strncpy(new_entry->name, curr_name, strlen(curr_name)+1);
					new_entry->name[strlen(curr_name)] = '\0';
					parent_dir_inode.links++;
					parent_dir_inode.entry_count++;
					parent_dir_inode.size += sizeof(struct a1fs_dentry);
					// In disk, set the parent dir inode
					memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * parent_dir_inode.inode_id , &parent_dir_inode, sizeof(a1fs_inode));
					updated = 1;
					if(clock_gettime(CLOCK_REALTIME, &(parent_dir_inode.mtime))){
						perror( "clock gettime" );
					};
					break;
				}
			}
		}
	}
	// Check if exceeds extends limits.
	if (parent_dir_inode.extents_count == 512){
		// Possibly could use defragmentation algo to stretch the length of extents for the inode.
		return -ENOSPC;
	}
	
	if(updated == -1){ // data blocks allocated for parent_dir is not enough, need new blocks for new entry
		// only add one new block each time
		int new_block_num = get_empty_block_index(fs);
		
		if (new_block_num == -1){
		return -ENOSPC;
		}
		// new extent
		struct a1fs_extent* new_extent = (struct a1fs_extent*)(fs->image + extent_table_start * A1FS_BLOCK_SIZE +
															sizeof(struct a1fs_extent) * parent_dir_inode.extents_count);
		new_extent->start = new_block_num;
		new_extent->count = 1;
		parent_dir_inode.extents_count++;
		
		// add entry into new extent data blocks
		struct a1fs_dentry* new_entry = (struct a1fs_dentry*)(fs->image + new_block_num * A1FS_BLOCK_SIZE);
		new_entry->ino = new_inode->inode_id;
		strncpy(new_entry->name, curr_name, strlen(curr_name)+1);
		new_entry->name[strlen(curr_name)] = '\0';
		if(clock_gettime(CLOCK_REALTIME, &(parent_dir_inode.mtime))){
		perror( "clock gettime" );
		};
		parent_dir_inode.links++;
		parent_dir_inode.entry_count++;
		parent_dir_inode.size += sizeof(struct a1fs_dentry);
	
		// set block occupied
		set_bitmap_by_index(block_bitmap, new_block_num);
		super_block->free_blocks_count --;

		// In disk, set the parent dir inode
		memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * parent_dir_inode.inode_id , &parent_dir_inode, sizeof(a1fs_inode));
		updated = 1;
	}
	
	if(updated == -1){
		printf("failed to add new entry when mkdir, space not enough");
		return -ENOSPC;
	}

	return 0;
}

/**
 * Remove a directory.
 *
 * Implements the rmdir() system call.
 *
 * Assumptions (already verified by FUSE using getattr() calls):
 *   "path" exists and is a directory.
 *
 * Errors:
 *   ENOTEMPTY  the directory is not empty.
 *
 * @param path  path to the directory to remove.
 * @return      0 on success; -errno on error.
 */
static int a1fs_rmdir(const char *path)
{
	fs_ctx *fs = get_fs();
	fprintf(stderr, "********* enter rmdir *********\n");
	//TODO: remove the directory at given path (only if it's empty)
	unsigned char* block_bitmap = fs->block_bitmap_address;
  	unsigned char* inode_bitmap = fs->inode_bitmap_address;
  	
	char dir_name[A1FS_NAME_MAX];
  	struct a1fs_inode parent_dir_inode;
	struct a1fs_inode file_inode;
	
  	getParentDirOfPathEnd(fs, path, &parent_dir_inode, dir_name);
	
	// grab the dir inode 
	for(unsigned int i = 0; i < parent_dir_inode.extents_count; i++){
		struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + parent_dir_inode.extent_table * A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent)*i);
		for(unsigned int j = 0; j < extent->count * A1FS_BLOCK_SIZE / sizeof(struct a1fs_dentry); j++){
			struct a1fs_dentry* entry = (struct a1fs_dentry*)(fs->image + extent->start*A1FS_BLOCK_SIZE + sizeof(struct a1fs_dentry)*j);
			if(strcmp(entry->name, dir_name)==0){ // find dir name entry in parent dir
				getInodeByID(fs, entry->ino, &file_inode); 
				//check if file is empty
				if (file_inode.size == 0){
					// remove entry from parent dir
					memset(entry, 0, sizeof(struct a1fs_dentry));  
				}
				else
				{
					fprintf(stderr, "the dir to be removed is not empty");
					fprintf(stderr, " \n ************* Get out removeDir    ************\n");
					return -ENOTEMPTY;
				}
				break;
			}
		}	
	}

	// Part one: find parent dir, for parent dir: update 1-size, 2-modification time, 3-entry count, 4-reset file entry ino as 0, 5-number of links -> memcpy parent inode to disk
	parent_dir_inode.size -= sizeof(a1fs_dentry);

	if(clock_gettime(CLOCK_REALTIME, &(parent_dir_inode.mtime))){
            perror( "clock gettime" );
    };

	parent_dir_inode.entry_count --;
	parent_dir_inode.links --;
	// memcpy parent inode to disk
	memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * parent_dir_inode.inode_id , &parent_dir_inode, sizeof(a1fs_inode)); 

	// Part two: for file: reset inode bitmap, block bitmap(extent table + real data blocks)
	// reset inode bitmap
	reset_bitmap_by_index(inode_bitmap, file_inode.inode_id);
	fs->super_block->free_inodes_count ++;

	// reset all real data block bitmap
	for(unsigned int i = 0; i < file_inode.extents_count; i++){
		struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + file_inode.extent_table * A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent) * i);
		unsigned char* data_start = (unsigned char*)(fs->image + extent->start*A1FS_BLOCK_SIZE);
		memset(data_start, 0, extent->count * A1FS_BLOCK_SIZE);
		// free all data blocks for each extent
		// fprintf(stderr, "\n *********** Remove!!!! extent start %d****************\n", extent->start);
		for(unsigned int j = 0; j < extent->count; j++){
			reset_bitmap_by_index(block_bitmap, extent->start + j);
			fs->super_block->free_blocks_count++;
		// fprintf(stderr, "\n *********** remove data block %d****************\n", extent->start + j + 1);
		}
	}


	// reset extent table block
	//fprintf(stderr, "\n remove extent table, at block %d \n", file_inode->extent_table);
	reset_bitmap_by_index(block_bitmap, file_inode.extent_table);
	fs->super_block->free_blocks_count++;
	struct a1fs_extent* extent_table = (struct a1fs_extent*)(fs->image + file_inode.extent_table * A1FS_BLOCK_SIZE);
	memset(extent_table, 0, A1FS_BLOCK_SIZE);

	fprintf(stderr, " \n ************* Get out removeDir   ************\n");
	return 0;
}

/**
 * Create a file.
 *
 * Implements the open()/creat() system call.
 *
 * Assumptions (already verified by FUSE using getattr() calls):
 *   "path" doesn't exist.
 *   The parent directory of "path" exists and is a directory.
 *   "path" and its components are not too long.
 *
 * Errors:
 *   ENOMEM  not enough memory (e.g. a malloc() call failed).
 *   ENOSPC  not enough free space in the file system.
 *
 * @param path  path to the file to create.
 * @param mode  file mode bits.
 * @param fi    unused.
 * @return      0 on success; -errno on error.
 */
static int a1fs_create(const char *path, mode_t mode, struct fuse_file_info *fi)
{
	(void)fi;// unused
	assert(S_ISREG(mode));
	fs_ctx *fs = get_fs();
	
	//TODO: create a file at given path with given mode
	fprintf(stderr, "\n *************  Enter creat, the  path %s  ************\n", path);
	//unsigned char* image = fs->image;
	struct a1fs_superblock* super_block = (struct a1fs_superblock*)fs->image;
	unsigned char* block_bitmap = fs->block_bitmap_address;
	unsigned char* inode_bitmap = fs->inode_bitmap_address;
	unsigned char* inode_table = fs->inode_table_address;
	
	// --------- create new inode -----------
	
	// new inode for new file
	int new_inode_id = get_empty_inode_ID(fs);
	if(new_inode_id == -1){
		printf("all inodes are in use");
		return -ENOSPC;
	}
	
	// for the inode, find the extent table block
	int new_extent_table_block_num = get_empty_block_index(fs);
	if(new_extent_table_block_num == -1){
		printf("all data block are in use");
		return -ENOSPC;
	}
	// fprintf(stderr, "*****make directory new_extent_table_block_at %u*************************\n", new_extent_table_block_num);
	
	// inode id from 0 to curr_inodes_count are in use, get new inode id
	// update curr_inodes_count by 1 increment
	// if(new_inode_id > fs->curr_inodes_count){
	//   fs->curr_inodes_count++;
	// }
	super_block->free_inodes_count --;
	super_block->free_blocks_count --;
	set_bitmap_by_index(inode_bitmap, new_inode_id);
	set_bitmap_by_index(block_bitmap, new_extent_table_block_num);
	
	// create new inode
	struct a1fs_inode* new_inode = (struct a1fs_inode*)(inode_table + sizeof(struct a1fs_inode)*(new_inode_id));
	new_inode->inode_id = new_inode_id;
	//fprintf(stderr, "new inode is %u\n", new_inode->inode_id);
	
	if((mode | S_IFREG) != 0){
		new_inode->mode = S_IFREG;
	};
	
	// if (new_inode->mode == S_IFREG){
	// 	fprintf(stderr, "mode is file when create file\n");
	// }
	
	// Initial link number for an file is 1.
	new_inode->links = 1;
	new_inode->size = 0; // 0 bytes data contained
	
	if(clock_gettime(CLOCK_REALTIME, &(new_inode->mtime))){
		perror( "clock gettime" );
	};
	
	// unsigned char* data_block_start = fs->real_data_blocks_sp;
	new_inode->extent_table = new_extent_table_block_num;
	new_inode->extents_count = 0;
	// Since there is no entry for regular file.
	// new_inode->entry_count = 0;
	
	
	// ---------- update parent_dir ------------
	char curr_name[A1FS_NAME_MAX];
	struct a1fs_inode parent_dir_inode;
	
	getParentDirOfPathEnd(fs, path, &parent_dir_inode, curr_name);
	// // FOR TESTING ONLY
	// fprintf(stderr,"Modify: %ld\n", parent_dir_inode.mtime.tv_sec);
	// fprintf(stderr, "**** 14 **********\n");
	// fprintf(stderr, "parent inode id: %u\n",parent_dir_inode.inode_id);
	
	// find extent_table for parent_dir inode
	int extent_table_start = parent_dir_inode.extent_table;
	
	//iterate all extents, find empty one, the maximum number of extents of an inode is 512.
	int updated = -1;
	
	char temp_path[A1FS_PATH_MAX];
	strncpy(temp_path, path, strlen(path)+1);
	temp_path[strlen(path)] = '\0';
	
	// FOR TESTING ONLY//////////////
	// fprintf(stderr,"Modify: %ld\n", parent_dir_inode.mtime.tv_sec);
	
	for(unsigned int i = 0; i < parent_dir_inode.extents_count; i++){//loop all extent
		if (updated == -1) {
		struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + extent_table_start * A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent) * i);
		// Loop all directory entry for each inode.
		for(unsigned int j = 0; j < extent->count * A1FS_BLOCK_SIZE / sizeof(struct a1fs_dentry); j++){
			struct a1fs_dentry* new_entry = (struct a1fs_dentry*)(fs->image + extent->start*A1FS_BLOCK_SIZE + sizeof(struct a1fs_dentry)*j);
			if(new_entry->ino == 0){ // empty entry, can be used
				new_entry->ino = new_inode->inode_id;
				strncpy(new_entry->name, curr_name, strlen(curr_name)+1);
				new_entry->name[strlen(curr_name)] = '\0';
				// For a regular file that is created, don't increment link number for the parent directory.
				//parent_dir_inode.links++;
				parent_dir_inode.entry_count++;
				
				// flexible to change
				parent_dir_inode.size += sizeof(struct a1fs_dentry);
				// In disk, set the parent dir inode
				memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * parent_dir_inode.inode_id , &parent_dir_inode, sizeof(a1fs_inode));
				updated = 1;
				if(clock_gettime(CLOCK_REALTIME, &(parent_dir_inode.mtime))){
					perror( "clock gettime" );
				};
				break;
			}
		}
		}
	}
	
	// Check if exceeds extends limits.
	if (parent_dir_inode.extents_count == 512){
		// Possibly could use defragmentation algo to stretch the length of extents for the inode.
		// CORNER CASE: RESET THE BITMAP BACK TO ORGINAL ONE.
		return -ENOSPC;
  }
  
  if(updated == -1){ // data blocks allocated for parent_dir is not enough, need new blocks for new entry
    // only add one new block each time
    int new_block_num = get_empty_block_index(fs);
    if (new_block_num == -1){
      return -ENOSPC;
    }
    // new extent
    struct a1fs_extent* new_extent = (struct a1fs_extent*)(fs->image + extent_table_start * A1FS_BLOCK_SIZE +
                                                           sizeof(struct a1fs_extent) * parent_dir_inode.extents_count);
    new_extent->start = new_block_num;
    new_extent->count = 1;
    parent_dir_inode.extents_count++;
    
    // add entry into new extent data blocks
    struct a1fs_dentry* new_entry = (struct a1fs_dentry*)(fs->image + new_block_num * A1FS_BLOCK_SIZE);
    new_entry->ino = new_inode->inode_id;
    strncpy(new_entry->name, curr_name, strlen(curr_name)+1);
    new_entry->name[strlen(curr_name)] = '\0';
    if(clock_gettime(CLOCK_REALTIME, &(parent_dir_inode.mtime))){
      perror( "clock gettime" );
    };
    // parent_dir_inode.links++;
    parent_dir_inode.entry_count++;
    parent_dir_inode.size += sizeof(struct a1fs_dentry);
    
    
    // set block occupied
    super_block->free_blocks_count--;
    set_bitmap_by_index(block_bitmap, new_block_num);
    
    // In disk, set the parent dir inode
    memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * parent_dir_inode.inode_id , &parent_dir_inode, sizeof(a1fs_inode));
    updated = 1;
  }
  
  if(updated == -1){
    printf("failed to add new entry when mkdir, space not enough");
    // CORNER CASE: RESET THE BITMAP BACK TO ORGINAL ONE.
    return -ENOSPC;
  }
  
  return 0;
}

/**
 * Remove a file.
 *
 * Implements the unlink() system call.
 *
 * Assumptions (already verified by FUSE using getattr() calls):
 *   "path" exists and is a file.
 *
 * Errors: none
 *
 * @param path  path to the file to remove.
 * @return      0 on success; -errno on error.
 */
static int a1fs_unlink(const char *path)
{
	fs_ctx *fs = get_fs();
	fprintf(stderr, " \n ************* Enter Unlink, the path %s  ************\n", path);

	//TODO: remove the file at given path
  	unsigned char* block_bitmap = fs->block_bitmap_address;
  	unsigned char* inode_bitmap = fs->inode_bitmap_address;
  	
	char file_name[A1FS_NAME_MAX];
  	struct a1fs_inode parent_dir_inode;
	struct a1fs_inode file_inode;

  	
  	getParentDirOfPathEnd(fs, path, &parent_dir_inode, file_name);
	

	// Part one: find parent dir, for parent dir: update 1-size, 2-modification time, 3-entry count, 4-reset file entry ino as 0 -> memcpy parent inode to disk
	parent_dir_inode.size -= sizeof(a1fs_dentry);

	if(clock_gettime(CLOCK_REALTIME, &(parent_dir_inode.mtime))){
            perror( "clock gettime" );
    };

	parent_dir_inode.entry_count -=1;

	// Part two: for file: reset inode bitmap, block bitmap(extent table + real data blocks)
	// grab the file inode 
	for(unsigned int i = 0; i < parent_dir_inode.extents_count; i++){
		struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + parent_dir_inode.extent_table * A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent)*i);
		for(unsigned int j = 0; j < extent->count * A1FS_BLOCK_SIZE / sizeof(struct a1fs_dentry); j++){
			struct a1fs_dentry* entry = (struct a1fs_dentry*)(fs->image + extent->start*A1FS_BLOCK_SIZE + sizeof(struct a1fs_dentry)*j);
			if(strcmp(entry->name, file_name)==0){ // find file name entry in parent dir
				getInodeByID(fs, entry->ino, &file_inode); 
				memset(entry, 0, sizeof(struct a1fs_dentry));  // remove entry from parent dir
				break;
			}
		}
	}
	// memcpy parent inode to disk
	memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * parent_dir_inode.inode_id , &parent_dir_inode, sizeof(a1fs_inode)); 

	// reset inode bitmap
	reset_bitmap_by_index(inode_bitmap, file_inode.inode_id);
	fs->super_block->free_inodes_count ++;

	// reset all real data block bitmap
	for(unsigned int i = 0; i < file_inode.extents_count; i++){
		struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + file_inode.extent_table * A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent) * i);
		unsigned char* data_start = (unsigned char*)(fs->image + extent->start*A1FS_BLOCK_SIZE);
		memset(data_start, 0, extent->count * A1FS_BLOCK_SIZE);
		// free all data blocks for each extent
		// fprintf(stderr, "\n *********** Remove!!!! extent start %d****************\n", extent->start);
		for(unsigned int j = 0; j < extent->count; j++){
			reset_bitmap_by_index(block_bitmap, extent->start + j);
			fs->super_block->free_blocks_count++;
		// fprintf(stderr, "\n *********** remove data block %d****************\n", extent->start + j + 1);
		}
	}


	// reset extent table block
	//fprintf(stderr, "\n remove extent table, at block %d \n", file_inode->extent_table);
	reset_bitmap_by_index(block_bitmap, file_inode.extent_table);
	fs->super_block->free_blocks_count++;
	struct a1fs_extent* extent_table = (struct a1fs_extent*)(fs->image + file_inode.extent_table * A1FS_BLOCK_SIZE);
	memset(extent_table, 0, A1FS_BLOCK_SIZE);

	fprintf(stderr, " \n ************* Get out Unlink    path %s  ************\n", path);
	return 0;
}


/**
 * Change the modification time of a file or directory.
 *
 * Implements the utimensat() system call. See "man 2 utimensat" for details.
 *
 * NOTE: You only need to implement the setting of modification time (mtime).
 *
 * Assumptions (already verified by FUSE using getattr() calls):
 *   "path" exists.
 *
 * Errors: none
 *
 * @param path   path to the file or directory.
 * @param times  timestamps array. See "man 2 utimensat" for details.
 * @return       0 on success; -errno on failure.
 */
static int a1fs_utimens(const char *path, const struct timespec times[2])
{
	fs_ctx *fs = get_fs();
	fprintf(stderr,"********* Enter utimens, path is: %s *************\n", path);
	struct a1fs_inode targetInode;
	
  	get_target_inode_from_path(fs, path, &targetInode);

	// fprintf(stderr,"********* the target Inode id is: %d **************\n", targetInode.inode_id);

	if (times == NULL) {
		clock_gettime(CLOCK_REALTIME, &(targetInode.mtime));
		memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * targetInode.inode_id , &targetInode, sizeof(a1fs_inode));
	}
	else {
		targetInode.mtime.tv_sec = times[1].tv_sec;
		targetInode.mtime.tv_nsec = times[1].tv_nsec;
		memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * targetInode.inode_id , &targetInode, sizeof(a1fs_inode));
		// fprintf(stderr,"Modified Time is changed to: %ld, %ld\n", targetInode.mtime.tv_sec, targetInode.mtime.tv_nsec);
		// RECHECK IF IT IS MODIFIED IN ACTUAL INODE TABLE.
	}
	return 0;
}

/**
 * Change the size of a file.
 *
 * Implements the truncate() system call. Supports both extending and shrinking.
 * If the file is extended, the new uninitialized range at the end must be
 * filled with zeros.
 *
 * Assumptions (already verified by FUSE using getattr() calls):
 *   "path" exists and is a file.
 *
 * Errors:
 *   ENOMEM  not enough memory (e.g. a malloc() call failed).
 *   ENOSPC  not enough free space in the file system.
 *
 * @param path  path to the file to set the size.
 * @param size  new file size in bytes.
 * @return      0 on success; -errno on error.
 */
static int a1fs_truncate(const char *path, off_t size)
{
	fs_ctx *fs = get_fs();
	fprintf(stderr, "********* enter truncate *********\n");
	//TODO: set new file size, possibly "zeroing out" the uninitialized range
	unsigned char* block_bitmap = fs->block_bitmap_address;
	struct a1fs_superblock* super_block = fs->super_block;

	struct a1fs_inode file_inode;
	
  	get_target_inode_from_path(fs, path, &file_inode);
	
	// check file original size
	unsigned int file_origin_size = file_inode.size;

	// number of original data blocks
	unsigned int total_block_existing = get_the_total_blocks_number(fs, &file_inode);
	fprintf(stderr, "***************************** total block existing number is: %u***********************************\n", total_block_existing);
	unsigned int total_block_needed = (size / A1FS_BLOCK_SIZE) + (size % A1FS_BLOCK_SIZE > 0 ? 1 : 0);	
	fprintf(stderr, "***************************** total block needed number is: %u***********************************\n", total_block_needed);

	// update file inode size and modification time
	file_inode.size = size;
	if(clock_gettime(CLOCK_REALTIME, &(file_inode.mtime))){
      perror( "clock gettime" );
    };

	// Case 1: Expand. Original file size is smaller than given size, padding with 0, attach more empty datablock.
	if(file_origin_size < size){
		fprintf(stderr, "**********************************Enter Truncate Case 1 ***********************************\n");
		unsigned int number_block_needed = total_block_needed - total_block_existing;
		fprintf(stderr, "********************************** number of block needed is: %d ***********************************\n", number_block_needed);
		if (number_block_needed > 0){
			fprintf(stderr, "********************************** 2 ***********************************\n");

			// Update 1.size 2.modification time 3.add one/multiple extent(s) + add extent start and extent count + continous blocks 
			// 4.update block bitmap(update super block free blocks count) -> store the inode back to disk.
			

			//to find how many extents needed
			unsigned int number_of_extents_needed = 0;
		
			unsigned int extent_start, longest_count; 
		
			//call helper find_available_extents
			//find enough continous blocks for data, return 0, if not long enough, return -1 
			while (find_available_longest_blocks(fs, &number_block_needed, &extent_start, &longest_count) < 0){ //not find enough, keep searching
				fprintf(stderr, "********************************** 3 ***********************************\n");
				struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + file_inode.extent_table * A1FS_BLOCK_SIZE + (file_inode.extents_count + number_of_extents_needed) * sizeof(struct a1fs_extent));
				extent->start = extent_start;// where the real data block start
				extent->count = longest_count;// how the length for this extent
				//set block bit map
				for (unsigned int i = 0; i < longest_count; i++){
					set_bitmap_by_index(block_bitmap, extent_start+i);
					super_block->free_blocks_count--;
				}
				number_of_extents_needed++;
			}	
			fprintf(stderr, "********************************** 4 ***********************************\n");
			fprintf(stderr, "********************************** 5 new extent start from %u, length is %u ***********************************\n", extent_start, number_block_needed);

			struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + file_inode.extent_table * A1FS_BLOCK_SIZE + (file_inode.extents_count + number_of_extents_needed) * sizeof(struct a1fs_extent));
			number_of_extents_needed++;
			extent->start = extent_start;
			extent->count = number_block_needed;
			//set block bit map		
			for (unsigned int i = 0; i < number_block_needed; i++){
				set_bitmap_by_index(block_bitmap , extent_start + i);
				super_block->free_blocks_count--;
			}

			file_inode.extents_count += number_of_extents_needed;

			if (file_inode.extents_count > 512){
				return -ENOSPC;
			}
		}

		//do not need more block
		else{
			// Update 1-size(done) 2.modification time(done) -> store the inode back to disk(will be done later).
			// So leave empty bracket here 
		}
	}
	// Case 2: Shrink. Original file size is larger than given size, cut data.
	// TO DO
	else if(file_origin_size > size){
		fprintf(stderr, "**********************************Enter Truncate Case 2 ***********************************\n");
		// 1-size(done) 2-modification time(done) 3-extent + extents count(if in need, note that this is the number of extent)

		// locate total block needed
		unsigned int count = 0;
		unsigned int extent_num = 0;
		while(count < total_block_needed){
			// grab extent, modify extent and store extent back to disk
			struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + file_inode.extent_table*A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent) * extent_num);
			unsigned int extent_count = extent->count;

			if((count + extent_count) <= total_block_needed){
				count += extent_count;
			}
			else
			{
				//free block bitmap
				for(unsigned int j = total_block_needed - count; j < extent->count; j++){
					reset_bitmap_by_index(block_bitmap, extent->start + j);
					fs->super_block->free_blocks_count++;
				}
				extent->count = total_block_needed - count;
				if (extent->count == 0){
					//reset this extent to initialized setting
					extent->start = 0;
					file_inode.extents_count--;
				}
				//store extent back to disk
				memcpy(fs->image + file_inode.extent_table*A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent) * extent_num, extent, sizeof(a1fs_extent));
				count = total_block_needed;
			}
			extent_num ++;
		}
	}
	//store inode to disk back
	memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * file_inode.inode_id , &file_inode, sizeof(a1fs_inode));

	fprintf(stderr, "********* get out from truncate *********\n");		

	//test
	fprintf(stderr, "********* 6 file inode extents count is: %d *********\n", file_inode.extents_count);		

	struct a1fs_extent* first_extent = (struct a1fs_extent*)(fs->image + file_inode.extent_table*A1FS_BLOCK_SIZE);
	fprintf(stderr, "********** 7 file inode first extent, start from %u, length is %u***********************************\n", first_extent->start, first_extent->count);


	fprintf(stderr, "print inode bitmap\n");
  	print_bitmap(fs->inode_bitmap_address, fs->super_block->inodes_count);

  	fprintf(stderr, "print block bitmap\n");
  	print_bitmap(fs->block_bitmap_address, fs->super_block->blocks_count);
	return 0;
}


/**
 * Read data from a file.
 *
 * Implements the pread() system call. Must return exactly the number of bytes
 * requested except on EOF (end of file). Reads from file ranges that have not
 * been written to must return ranges filled with zeros. You can assume that the
 * byte range from offset to offset + size is contained within a single block.
 *
 * Assumptions (already verified by FUSE using getattr() calls):
 *   "path" exists and is a file.
 *
 * Errors: none
 *
 * @param path    path to the file to read from.
 * @param buf     pointer to the buffer that receives the data.
 * @param size    buffer size (number of bytes requested).
 * @param offset  offset from the beginning of the file to read from.
 * @param fi      unused.
 * @return        number of bytes read on success; 0 if offset is beyond EOF;
 *                -errno on error.
 */
static int a1fs_read(const char *path, char *buf, size_t size, off_t offset,
                     struct fuse_file_info *fi)
{
	(void)fi;// unused
	fs_ctx *fs = get_fs();
	
	// TODO: read data from the file at given offset into the buffer
	fprintf(stderr, "\n **************** Enter read ***************\n");
	// Find the inode based on the path
	struct a1fs_inode fileInode;
	get_target_inode_from_path(fs, path, &fileInode);
	
	// Type check
	if (fileInode.mode == S_IFREG){
		fprintf(stderr, "target is a true file");
	}else{
		perror("target is not a file");
	}
	
	// Offset check
	if(offset >= (off_t)fileInode.size){
		fprintf(stderr, "\n offset exceed file size \n");
		return 0;
	}
	
	// Check if file size - offset < request size, if so padding with 0 to buffer
	if((fileInode.size - offset) < size){
		fprintf(stderr, "\n ***************Enter the first case of Read*******************\n");
		memset(buf, 0, size);
		// First read all data from all related data blocks
		unsigned int total_block = get_the_total_blocks_number(fs, &fileInode);
		char temp_buffer[total_block * A1FS_BLOCK_SIZE];

		char * temp_buffer_ptr = temp_buffer;
		//int total_data_block_count = 0;

		for(unsigned int i = 0; i < fileInode.extents_count; i++){
			struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + fileInode.extent_table * A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent) * i);
			//unsigned int extent_blocks_count = extent->count;
			//total_data_block_count += extent_blocks_count;
			unsigned char* extent_data_start_ptr = (unsigned char*)(fs->image + extent->start * A1FS_BLOCK_SIZE);
			memcpy(temp_buffer_ptr, extent_data_start_ptr, (extent->count) * A1FS_BLOCK_SIZE);
			temp_buffer_ptr += (extent->count) * A1FS_BLOCK_SIZE;
		}
		memcpy(buf, temp_buffer + offset, fileInode.size - offset);
		fprintf(stderr, "\n **************** Great, get out from read ***************\n");
		return size;
	}
	// (file size - offset) >= request size, no padding
	else{
		fprintf(stderr, "\n ***************Enter the second case of Read*******************\n");
		char temp_buffer[fileInode.size];
		char * temp_buffer_ptr = temp_buffer;
		//int total_data_block_count = 0;
		for(unsigned int i = 0; i < fileInode.extents_count; i++){
			struct a1fs_extent* extent = (struct a1fs_extent*)(fs->image + fileInode.extent_table * A1FS_BLOCK_SIZE + sizeof(struct a1fs_extent)*i);
			//unsigned int extent_blocks_count = extent->count;
			//total_data_block_count += extent_blocks_count;
			unsigned char* extent_data_start_ptr = (unsigned char*)(fs->image + extent->start * A1FS_BLOCK_SIZE);
			memcpy(temp_buffer_ptr, extent_data_start_ptr, (extent->count) * A1FS_BLOCK_SIZE);
			temp_buffer_ptr += (extent->count) * A1FS_BLOCK_SIZE;
		}
		memcpy(buf, temp_buffer + offset, size);
		fprintf(stderr, "\n **************** Great, get out from read ***************\n");
		return size;
  }
}

/**
 * Write data to a file.
 *
 * Implements the pwrite() system call. Must return exactly the number of bytes
 * requested except on error. If the offset is beyond EOF (end of file), the
 * file must be extended. If the write creates a "hole" of uninitialized data,
 * the new uninitialized range must filled with zeros. You can assume that the
 * byte range from offset to offset + size is contained within a single block.
 *
 * Assumptions (already verified by FUSE using getattr() calls):
 *   "path" exists and is a file.
 *
 * Errors:
 *   ENOMEM  not enough memory (e.g. a malloc() call failed).
 *   ENOSPC  not enough free space in the file system.
 *
 * @param path    path to the file to write to.
 * @param buf     pointer to the buffer containing the data.
 * @param size    buffer size (number of bytes requested).
 * @param offset  offset from the beginning of the file to write to.
 * @param fi      unused.
 * @return        number of bytes written on success; -errno on error.
 */
static int a1fs_write(const char *path, const char *buf, size_t size,
                      off_t offset, struct fuse_file_info *fi)
{
	(void)fi;// unused
	fs_ctx *fs = get_fs();
	fprintf(stderr, "********* enter write *********\n");

	fprintf(stderr, "********* print buffer content %s *********\n", buf);
	fprintf(stderr, "********* print buffer size %lu *********\n", strlen(buf));

	//TODO: write data from the buffer into the file at given offset, possibly
	// "zeroing out" the uninitialized range

	// 1-size 2-modification time 3-write data ->store file inode back into disk

	if(size == 0){
    return 0;
	}

	if (size > fs->super_block->free_blocks_count * A1FS_BLOCK_SIZE){
		return -ENOSPC;
	}

	struct a1fs_inode temp_fileInode;
  	get_target_inode_from_path(fs, path, &temp_fileInode);

	if(offset + size > temp_fileInode.size){
    	int res = a1fs_truncate(path, offset + size);
		if(res != 0){
			return -ENOSPC;
		}
  	}

	struct a1fs_inode fileInode;
  	get_target_inode_from_path(fs, path, &fileInode);
	
	// locate the offset location
	unsigned int target_extent_num = 0;
	unsigned int target_extent_start_block;
	unsigned int target_extent_len;
	unsigned int final_offset_count;
	off_t offset_count = offset;
	bool if_found_offset = false;

	while(! if_found_offset){
		struct a1fs_extent* extent = (a1fs_extent*)(fs->image + fileInode.extent_table * A1FS_BLOCK_SIZE + sizeof(a1fs_extent) * target_extent_num);
		a1fs_blk_t block_start = extent->start;
		a1fs_blk_t block_count = extent->count;
		// find the offset in current extent territory
		if (block_count * A1FS_BLOCK_SIZE >= offset_count){
			if_found_offset = true;
			target_extent_start_block = block_start;
			target_extent_len = offset_count / A1FS_BLOCK_SIZE;
			final_offset_count = (unsigned int)(offset_count % A1FS_BLOCK_SIZE);
		}

		if(! if_found_offset){
			offset_count -= block_count * A1FS_BLOCK_SIZE;
			target_extent_num ++;
		}
	}

	// write data from buffer to disk
	struct a1fs_extent* extent = (a1fs_extent*)(fs->image + fileInode.extent_table * A1FS_BLOCK_SIZE + sizeof(a1fs_extent) * target_extent_num);
	//calculate the maximum potential space in this extent territory from final_offset to write.
	unsigned int max_space = (extent->count - target_extent_len) * A1FS_BLOCK_SIZE - final_offset_count;

	// based on assumption, the byte range from offset to offset + size is contained within a single block.
	if(max_space >= size){
		unsigned char* des_address = fs->image + (target_extent_start_block + target_extent_len) * A1FS_BLOCK_SIZE + final_offset_count;
		memcpy(des_address, buf, size);
		if(clock_gettime(CLOCK_REALTIME, &(fileInode.mtime))){
      		perror( "clock gettime" );
    	};
		memcpy(fs->inode_table_address + sizeof(struct a1fs_inode) * fileInode.inode_id , &fileInode, sizeof(a1fs_inode));
		fprintf(stderr, "-------Get out from write--------");
		return size;
	}
	
	// above assumption fail
	fprintf(stderr, "-------Write assumption failed--------");
	return -ENOSPC;
}


static struct fuse_operations a1fs_ops = {
	.destroy  = a1fs_destroy,
	.statfs   = a1fs_statfs,
	.getattr  = a1fs_getattr,
	.readdir  = a1fs_readdir,
	.mkdir    = a1fs_mkdir,
	.rmdir    = a1fs_rmdir,
	.create   = a1fs_create,
	.unlink   = a1fs_unlink,
	.utimens  = a1fs_utimens,
	.truncate = a1fs_truncate,
	.read     = a1fs_read,
	.write    = a1fs_write,
};

int main(int argc, char *argv[])
{
	a1fs_opts opts = {0};// defaults are all 0
	struct fuse_args args = FUSE_ARGS_INIT(argc, argv);
	if (!a1fs_opt_parse(&args, &opts)) return 1;

	fs_ctx fs = {0};
	if (!a1fs_init(&fs, &opts)) {
		fprintf(stderr, "Failed to mount the file system\n");
		return 1;
	}

	return fuse_main(args.argc, args.argv, &a1fs_ops, &fs);
}
