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
 * CSC369 Assignment 1 - a1fs formatting tool.
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>
#include <time.h>
#include "a1fs.h"
#include "map.h"
#include "util.h"

/** Command line options. */
typedef struct mkfs_opts {
  /** File system image file path. */
  const char *img_path;
  /** Number of inodes. */
  size_t n_inodes;
  
  /** Print help and exit. */
  bool help;
  /** Overwrite existing file system. */
  bool force;
  /** Zero out image contents. */
  bool zero;
  
} mkfs_opts;

static const char *help_str = "\
Usage: %s options image\n\
\n\
Format the image file into a1fs file system. The file must exist and\n\
its size must be a multiple of a1fs block size - %zu bytes.\n\
\n\
Options:\n\
-i num  number of inodes; required argument\n\
-h      print help and exit\n\
-f      force format - overwrite existing a1fs file system\n\
-z      zero out image contents\n\
";

static void print_help(FILE *f, const char *progname)
{
  fprintf(f, help_str, progname, A1FS_BLOCK_SIZE);
}


static bool parse_args(int argc, char *argv[], mkfs_opts *opts)
{
  char o;
  while ((o = getopt(argc, argv, "i:hfvz")) != -1) {
    switch (o) {
      case 'i': opts->n_inodes = strtoul(optarg, NULL, 10); break;
        
      case 'h': opts->help  = true; return true;// skip other arguments
      case 'f': opts->force = true; break;
      case 'z': opts->zero  = true; break;
        
      case '?': return false;
      default : assert(false);
    }
  }
  
  if (optind >= argc) {
    fprintf(stderr, "Missing image path\n");
    return false;
  }
  opts->img_path = argv[optind];
  
  if (opts->n_inodes == 0) {
    fprintf(stderr, "Missing or invalid number of inodes\n");
    return false;
  }
  return true;
}


/** Determine if the image has already been formatted into a1fs. */
static bool a1fs_is_present(void *image)
{
  //TODO: check if the image already contains a valid a1fs superblock
  assert(image != NULL);
  
  a1fs_superblock *superblock = (a1fs_superblock *)image;
  if (A1FS_MAGIC == superblock->magic) {
    return true;
  }
  return false;
}


/**
 * Format the image into a1fs.
 *
 * NOTE: Must update mtime of the root directory.
 *
 * @param image  pointer to the start of the image.
 * @param size   image size in bytes.
 * @param opts   command line options.
 * @return       true on success;
 *               false on error, e.g. options are invalid for given image size.
 */
static bool mkfs(void *image, size_t size, mkfs_opts *opts)
{
  //TODO: initialize the superblock and create an empty root directory
  //NOTE: the mode of the root directory inode should be set to S_IFDIR | 0777
  assert(image != NULL);
  assert(opts != NULL);
  
  if (opts->n_inodes <4) {
    return false;
  }
  
  // Check if the allcated disk size is sufficient to construct the given file system structure (e.g inodes, extent table, etc.)
  a1fs_blk_t total_block_number = size / A1FS_BLOCK_SIZE;
  a1fs_blk_t inodes_count = opts->n_inodes;
  a1fs_blk_t inodes_bitmap_blocks_count = opts->n_inodes / (A1FS_BLOCK_SIZE * 8) + (opts->n_inodes  % (A1FS_BLOCK_SIZE * 8) > 0 ? 1 : 0);
  a1fs_blk_t block_bitmap_blocks_count = size / (A1FS_BLOCK_SIZE * A1FS_BLOCK_SIZE * 8) + (size % (A1FS_BLOCK_SIZE * A1FS_BLOCK_SIZE * 8) > 0 ? 1 : 0);
  a1fs_blk_t inode_table_blocks_count = inodes_count * sizeof(struct a1fs_inode) / A1FS_BLOCK_SIZE + (opts->n_inodes * sizeof(struct a1fs_inode) % A1FS_BLOCK_SIZE > 0 ? 1 : 0);
  

  // Check if sufficient space is allocated for the image.
  // 2 - one for super block, one for first extent table
  if (total_block_number < 2 + inodes_bitmap_blocks_count + inode_table_blocks_count + block_bitmap_blocks_count) {
    return false;
  }

  // number of blocks for real data block
  // a1fs_blk_t blocks_count = total_block_number - inodes_bitmap_blocks_count - inode_table_blocks_count - block_bitmap_blocks_count;
  
  
  // initilize whole image as 0
  memset(image, 0, size);
    
    
  /** File system size in bytes. */
  size = (uint64_t)size;
  a1fs_blk_t free_inodes_count = opts->n_inodes - 1;
  
  a1fs_blk_t   inode_bitmap = 1;
  a1fs_blk_t   block_bitmap = 1 + inodes_bitmap_blocks_count;
  a1fs_blk_t   inode_table = 1 + inodes_bitmap_blocks_count + block_bitmap_blocks_count;

  // 1 - superblock, 1 - first extent table for root inode
  a1fs_blk_t free_blocks_count = total_block_number - 1 - inodes_bitmap_blocks_count - block_bitmap_blocks_count -
  inode_table_blocks_count - 1;
  
  a1fs_blk_t data_block = inode_table + inode_table_blocks_count;

  
  // Initiate the superblock
  a1fs_superblock superblock = {A1FS_MAGIC, size, inode_bitmap, block_bitmap, inode_table, data_block, inodes_count,
   total_block_number, free_blocks_count, free_inodes_count, inodes_bitmap_blocks_count, block_bitmap_blocks_count, 
   inode_table_blocks_count};
  
  // Attach the superbock at the image beginning address
  memcpy(image, &superblock, sizeof(superblock));
  
  // Initialize inode bitmap and block bitmap to 0
  memset(image + A1FS_BLOCK_SIZE, 0, (inodes_bitmap_blocks_count + block_bitmap_blocks_count) * A1FS_BLOCK_SIZE);
  
  // Starting point of block bitmap
  unsigned char* block_bitmap_address = (unsigned char*)(image + block_bitmap * A1FS_BLOCK_SIZE);
  
  // current used block number
  int bit, byte;
  int count = 1 + inodes_bitmap_blocks_count + block_bitmap_blocks_count + inode_table_blocks_count;
  int byte_count = count / 8 + (count % 8 > 0 ? 1 : 0);

  // fprintf(stderr, "test, count%d\n", count);

  for (byte = 0; byte < byte_count; byte++){
    for(bit = 0; bit < 8; bit++){
      if (count > 0){
        block_bitmap_address[byte] |= 1<<bit;
        count--;
      }
    }
  }
  // fprintf(stderr, "test, first time print block bitmap\n");
  // print_bitmap(block_bitmap_address, total_block_number);

  // initialize inode structs
  a1fs_blk_t i;
  for (i = 0; i < opts->n_inodes; i++)
  {
    a1fs_inode new_inode={0};
    memcpy(image + (1 + inodes_bitmap_blocks_count + block_bitmap_blocks_count) * A1FS_BLOCK_SIZE +
           i * sizeof(struct a1fs_inode), &new_inode, sizeof(struct a1fs_inode));
  }
  
  // Initiate root inode address
  struct a1fs_inode* root_inode = (struct a1fs_inode*)(image + inode_table * A1FS_BLOCK_SIZE);
  
  root_inode->mode = S_IFDIR | 0777;
  
  // change inode bitmap[0] to be occupied
  // Starting point of inode bitmap
  unsigned char* inode_bitmap_address = (unsigned char*)(image + inode_bitmap * A1FS_BLOCK_SIZE);
  
  // in inode_bitmap, set first index as 1 for root dir inode
  //inode_bitmap_address[0] = inode_bitmap_address[0] | (1<<0);
  set_bitmap_by_index(inode_bitmap_address, 0);

  root_inode->inode_id = 0; // root dir inode's id is 0
  
  // set links, size, entry_count, mtime
  root_inode->links = 2; // There's one for the directory itself, and one for . inside it.
  root_inode->size = 0;
  
  // Initiate extent table for root_node and set the corresponding block bitmap to 1
  
  root_inode->extent_table = inode_table + inode_table_blocks_count;

  //block_bitmap_address[0] = block_bitmap_address[0] | (1<<(inode_table + inode_table_blocks_count));
  set_bitmap_by_index(block_bitmap_address, inode_table + inode_table_blocks_count);

  root_inode->extents_count = 0;
  
  root_inode->entry_count = 0;
  
  if(clock_gettime(CLOCK_REALTIME, &(root_inode->mtime))){
    perror( "clock gettime" );
  };
  //
  //fprintf(stderr,"First created time: %ld\n", root_inode->mtime.tv_sec);
  
  

  return true;
}


int main(int argc, char *argv[])
{
  mkfs_opts opts = {0};// defaults are all 0
  if (!parse_args(argc, argv, &opts)) {
    // Invalid arguments, print help to stderr
    print_help(stderr, argv[0]);
    return 1;
  }
  if (opts.help) {
    // Help requested, print it to stdout
    print_help(stdout, argv[0]);
    return 0;
  }
  
  // Map image file into memory
  size_t size;
  void *image = map_file(opts.img_path, A1FS_BLOCK_SIZE, &size);
  if (image == NULL) return 1;
  
  // Check if overwriting existing file system
  int ret = 1;
  if (!opts.force && a1fs_is_present(image)) {
    fprintf(stderr, "Image already contains a1fs; use -f to overwrite\n");
    goto end;
  }
  
  if (opts.zero) memset(image, 0, size);
  if (!mkfs(image, size, &opts)) {
    fprintf(stderr, "Failed to format the image\n");
    goto end;
  }
  
  ret = 0;
end:
  munmap(image, size);
  return ret;
}
