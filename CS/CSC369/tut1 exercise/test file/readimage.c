#include <fcntl.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <math.h>


#include "ext2.h"

#define FS1
#define FS2

struct bitmap {
	unsigned char array[EXT2_BLOCK_SIZE];
};

// Pointer to the beginning of the disk (byte 0)
static const unsigned char *disk = NULL;

static void print_blockgroup(const struct ext2_group_desc *group, int verbose)
{
	if (verbose)
	{
		printf("Block group:\n");
		printf("    block bitmap: %d\n", group->bg_block_bitmap);
		printf("    inode bitmap: %d\n", group->bg_inode_bitmap);
		printf("    inode table: %d\n", group->bg_inode_table);
		printf("    free blocks: %d\n", group->bg_free_blocks_count);
		printf("    free inodes: %d\n", group->bg_free_inodes_count);
		printf("    used_dirs: %d\n", group->bg_used_dirs_count);
	}
	else
	{
		printf("%d, %d, %d, %d, %d, %d\n",
			group->bg_block_bitmap,
		 	group->bg_inode_bitmap,
		 	group->bg_inode_table,
		 	group->bg_free_blocks_count,
		 	group->bg_free_inodes_count,
		 	group->bg_used_dirs_count);
	}
}

void print_usage()
{
	fprintf(stderr, "Usage: readimage [-tv] <image file name>\n");
	fprintf(stderr, "     -t will print the output in terse format for auto-testing\n");
	fprintf(stderr, "     -v will print the output in verbose format for easy viewing\n");
}

void print_bitmap(const struct bitmap *b, int end)
{
  int num_of_byte;
  int in_use_bit;
  int bit,byte;
  num_of_byte = end / 8;

  for (byte = 0; byte < num_of_byte; byte++) {
    for (bit = 0; bit < 8; bit++) {
		in_use_bit = b->array[byte] & (1 << bit);
      	if(in_use_bit >= 1){
				printf("1");
      	}
		else{
        printf("0");
      	}
    }

    if (byte != (num_of_byte - 1)) {
      printf(" ");
    }
  }
  printf("\n");

}

bool if_high_bitmap(const struct bitmap *inode_bitmap, int index_inode)
{  
  int index_array = index_inode / 8;
  int offset = index_inode - (index_array * 8);
  
  return inode_bitmap->array[index_array] & (1 << offset) ? true : false;
}

void print_inode(const struct ext2_inode *inode, int index, int verbose) {
  if (verbose) {
    printf("Inodes:\n");
  }
  
  printf("[%d]", index);
  
  if (verbose) {
    char mode_;
    if (inode->i_mode & EXT2_S_IFDIR){
      mode_ = 'd';
    }
    else{
      mode_ = 'f';
    }
    printf(" type: %c size: %d links: %d blocks: %d",
           mode_,
           inode->i_size,
           inode->i_links_count,
           inode->i_blocks
           );
  } else {
    char mode_;
    if (inode->i_mode & EXT2_S_IFDIR){
      mode_ = 'd';
    }
    else{
      mode_ = 'f';
    }
    printf(" %c, %d, %d, %d",
           mode_,
           inode->i_size,
           inode->i_links_count,
           inode->i_blocks
           );
  }
  
  if (verbose) {
    printf("\n");
    printf("[%d] Blocks: ", index);
  } else {
    printf(" | ");
  }
  
  int count = ceil(inode->i_blocks / 2.0);
  int cutoff = count;
  if (count > 12) {
    cutoff = 13;
  }
  
  for(int i = 1; i <= cutoff; i++)
  {
    if ((inode->i_size > (i-1) * EXT2_BLOCK_SIZE)) {
      printf(" %d", inode->i_block[i-1]);
    }
  }
  printf("\n");
}


int main(int argc, char *argv[])
{
	int option;
	int verbose = 1;
	while ((option = getopt(argc, argv, "tv")) != -1)
	{
		switch (option)
		{
		case 't':
			verbose = 0;
			break;
		case 'v':
			verbose = 1;
			break;
		default:
			print_usage();
			exit(1);
		}
	}

	if (optind >= argc)
	{
		print_usage();
		exit(1);
	}

	int fd = open(argv[optind], O_RDONLY);
	if (fd == -1)
	{
		perror("open");
		exit(1);
	}

	// Map the disk image into memory so that we don't have to do any reads and writes
	disk = mmap(NULL, 128 * EXT2_BLOCK_SIZE, PROT_READ, MAP_SHARED, fd, 0);
	if (disk == MAP_FAILED)
	{
		perror("mmap");
		exit(1);
	}

	const struct ext2_super_block *sb = (const struct ext2_super_block *)(disk + EXT2_BLOCK_SIZE);

	if (verbose)
	{
		printf("Inodes: %d\n", sb->s_inodes_count);
		printf("Blocks: %d\n", sb->s_blocks_count);
	}
	else
	{
		printf("%d, %d, ", sb->s_inodes_count, sb->s_blocks_count);
	}

	const struct ext2_group_desc *group = (const struct ext2_group_desc *)(disk + EXT2_BLOCK_SIZE * 2);
	print_blockgroup(group, verbose);

	/*TODO*/
	//Task 2
	const struct bitmap *block_bitmap = (const struct bitmap *)(disk + EXT2_BLOCK_SIZE * 3);
 	const struct bitmap *inode_bitmap = (const struct bitmap *)(disk + EXT2_BLOCK_SIZE * 4);

	if (verbose) {
    	printf("Block bitmap: ");
    	print_bitmap(block_bitmap, sb->s_blocks_count);

    	printf("Inode bitmap: ");
    	print_bitmap(inode_bitmap, sb->s_inodes_count);
  	} 
	else {
    	print_bitmap(block_bitmap, sb->s_blocks_count);
    	print_bitmap(inode_bitmap, sb->s_inodes_count);
  	}

	//task 3
	for (int i = 1; i < sb->s_inodes_count; i++) {
    // ignore the first 11
    if (i > 1 && i < 11) {
      continue;
    }
    
    int offset = sizeof(struct ext2_inode) * i;
    const struct ext2_inode *inode = (const struct ext2_inode *)(disk + EXT2_BLOCK_SIZE * 5 + offset);
    
    if (if_high_bitmap(inode_bitmap, i)) 
		{
      	print_inode(inode, i, verbose);
    	}
  	}
	return 0;
}
