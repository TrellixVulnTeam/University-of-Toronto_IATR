#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>

/* Hungry, hungry hippos! There are "players" hippos (4, in the board game, but
 * we can * imagine more). A referee dumps a handful of marbles ("total_marbles"
 * of them) between the hippos, and the hippos attempt to consume marbles as
 * quickly as possible.
 * However, each hippo can only consume one marble at a time. When all of the
 * marbles have been consumed, the hippo who ate the last marble informs the
 * referee, who prints the score for that round and then dumps "total_marbles"
 * more marbles onto the board. This game repeats for a fixed number of "rounds".
 *
 */

// Default values for variables
#define PLAYERS 50
#define MARBLES 1000
#define ROUNDS 5

int players = PLAYERS;
int total_marbles = MARBLES;
int marbles = MARBLES;
int rounds = ROUNDS;
int *scores;

/* Synchronization Declarations */
pthread_mutex_t region_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t out_of_marbles = PTHREAD_COND_INITIALIZER;
pthread_cond_t done_game = PTHREAD_COND_INITIALIZER;

/*  Do not modify this function.  It does not need any synchronization */
void print_and_clear_scores() {
  int i;
  int sum = 0;
  printf("Scores:\n");
  for(i = 0; i < players; i++) {
    printf("%d ", scores[i]);
    sum += scores[i];
    scores[i] = 0;
  }
  printf(" SUM= %d\n", sum);
}
void eat(int id){
	pthread_mutex_lock(&region_mutex);
	// If the marbles are all gone then wait for the game to restart
	// Need another condition if there will be no more rounds
	
	while(marbles == 0) {
		pthread_cond_wait(&out_of_marbles, &region_mutex);
		pthread_mutex_unlock(&region_mutex);
		return;
		// while (rounds == 0){
		// pthread_cond_wait(&done_game, &region_mutex);
		// pthread_mutex_unlock(&region_mutex);
		// return;
		//}
	}
	
	// Need a way to return if there are no more rounds (remember to unlock)
	
	// Take turn
	marbles--;
	scores[id]++;

	

	if(marbles == 0){
		pthread_cond_signal(&out_of_marbles);
	}
	pthread_mutex_unlock(&region_mutex);
}

void restart_game() {
  
  pthread_mutex_lock(&region_mutex);
  while(marbles != 0){
    pthread_cond_wait(&out_of_marbles, &region_mutex);
  }
  
  print_and_clear_scores();
  marbles = total_marbles;
  
  pthread_cond_broadcast(&out_of_marbles);
  pthread_mutex_unlock(&region_mutex);
}

/* This is the main function of the hippo threads. Do not modify this function.
 * All synchronization for the hippos will be added to the eat function.
 */

void *hippo(void *id_ptr) {
  long int id = (long int)id_ptr;
  /* Even though rounds is a shared variable, only the referee updates it
   * and there is no harm if the hippo calls eat after the referee sets
   * rounds to 0
   */
  while(rounds) {
    eat(id);
  }
  
  fprintf(stderr, "hippo %ld exiting\n", id);
  pthread_exit(NULL);
}

/* This is the main function of the referee thread.  The referee restarts the
 * game rounds times and then terminates.
 * Some code needs to be added to make sure that the hippo threads aren't  
 * waiting for a game continue or a new game to start before the referee exits.
 */

void *referee(void *id_ptr) {
	while(rounds)  {
		restart_game();
		rounds--;
	}
	
	pthread_cond_broadcast(&out_of_marbles);
	pthread_cond_signal(&done_game);

	fprintf(stderr, "referee exiting\n");
	return NULL;
}

int main(int argc, char **argv) {
  
  if(argc != 1 && argc != 4) {
    fprintf(stderr, "Usage: hippos [players marbles rounds]\n");
    fprintf(stderr, "      (With no arguments, use default values)\n");
    exit(1);
  } else if(argc == 4) {
    players = (int)strtod(argv[1], NULL);
    total_marbles = (int)strtod(argv[2], NULL);
    marbles = total_marbles;
    rounds = (int)strtod(argv[3], NULL);
  }
  
  pthread_t hippos[players];
  pthread_t ref;
  scores = malloc(sizeof(int)* players);
  
  long i;
  for(i = 0; i < players; i++) {
    scores[i] = 0;
  }
  
  // Create the players and the referee
  for(i = 0; i < players; i++) {
    pthread_create(&hippos[i], NULL, hippo, (void *)i);
  }
  pthread_create(&ref, NULL, referee, NULL);
  
  // Wait for the players and referee to terminate
  for(i = 0; i < players; i++) {
    pthread_join(hippos[i], NULL);
  }
  pthread_join(ref, NULL);
  free(scores);
  fprintf(stderr, "main thread exiting\n");
  pthread_exit(NULL);
}
