#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

// [ 8 marks]
/* At U of T day, student volunteers guide visitors to the Computer Science
 * Department.  A guide waits at the booth until N visitors arrive, and
 * then takes exactly N visitors on a tour.  If no guides are available or if
 * there are more than N visitors, then the visitors will wait until a guide comes.
 *
 * To ensure that the program terminates, the total number of visitors will always
 * be a multiple of N. Examples: "./tour 3 12"  or "./tour 4 8"
 *
 * Complete the program below that uses condition variables to solve this problem
 * You will need to add more synchronization variables, but should not need to add
 * any more regular variables.
 * 
 * Hint: Once there are enough visitors for a full tour, all threads waiting for
 * that tour should be awakened. This means you need to set the condition 
 * carefully.
 * 
 * The placement of the TODO comments are also intended to give you some big hints.
 * It is possible to earn part marks even if the solution is not fully correct, and
 * we will not be marking for style.
 * See sample_output.txt for example output
*/

pthread_mutex_t lock;
pthread_cond_t next_tour;

//Declare any additional locks and or conditional variables.
// TODO
pthread_cond_t guide_cond;
pthread_cond_t visitor_cond;
// These two variable specify the size of the problem and are arguments to main
// They remain constant throughout the program.
int tour_size = 0;
int max_visitors = 0;

int num_visitors = 0;

void *visitor(void *id) {
    long int myid = (long int)id;
    pthread_mutex_lock(&lock);
    
    // If there are already enough visitors to make up a full tour
    // wait until that tour has left.
    while(num_visitors == tour_size) {
        pthread_cond_wait(&next_tour, &lock);
    }

    // Note: num_visitors < tour_size at this point due to the previous wait
    num_visitors++;
    printf("Visitor %ld ready for tour\n", myid);

    // Wait until there are enough visitors for a full tour
    //TODO
    while (num_visitors < tour_size){
       pthread_cond_wait(&visitor_cond, &lock);
       pthread_mutex_unlock(&lock);
        pthread_exit(0);
    }

    if (num_visitors == tour_size){
        
        pthread_cond_signal(&guide_cond);

                
        pthread_mutex_unlock(&lock);
        pthread_exit(0);
    }
    // pthread_cond_broadcast(&visitor_cond);
    // pthread_cond_signal(&guide_cond);
        

    //pthread_cond_signal(&guide_cond);
    // Go on tour...
    // visitor is finished
    // pthread_mutex_unlock(&lock);
    // pthread_exit(0);
}

void *guide(void *id) {
    int i;
    // max_visitors will always be a multiple of tour_size
    for(i = 0; i < max_visitors/tour_size; i++) {
        // Wait until enough visitors arrive and then allow the visitors on the
        // tour to continue running.
        //TODO
        pthread_mutex_lock(&lock);

        while(num_visitors < tour_size){
            pthread_cond_wait(&guide_cond, &lock);
        }

        printf("Guide leading tour %d\n", i);
        num_visitors = 0;
        
        // Ensure that any visitors who had to wait for the next tour can proceed
        //TODO
        pthread_cond_broadcast(&next_tour);
        pthread_cond_broadcast(&visitor_cond); 

        pthread_mutex_unlock(&lock);

    }
    pthread_exit(0);
}

int main(int argc, char *argv[]) {

    pthread_mutex_init(&lock, NULL);
    pthread_cond_init(&next_tour, NULL);

    // Initialize any other synchronization variables
    // TODO
    pthread_cond_init(&guide_cond, NULL);
    pthread_cond_init(&visitor_cond, NULL);
    // The rest of main just creates the threads and waits for them to complete
    // Don't change anything below this
    pthread_t guide_id;

    if(argc != 3) {
        fprintf(stderr, "Usage: tour <tour size> <max visitors>\n");
        exit(1);
    }

    tour_size = strtod(argv[1], NULL);
    max_visitors = strtod(argv[2], NULL);

    pthread_t visitors[max_visitors];

    long int i;
    for(i = 0; i < max_visitors; i++) {
        pthread_create(&visitors[i], NULL, visitor, (void *)i);
    }
    pthread_create(&guide_id, NULL, guide, (void *)NULL);

    long int j;
    for(j = 0; j < max_visitors; j++) {
        pthread_join(visitors[j], NULL);
        printf("Visitor %ld left\n", j);
    }
    sleep(1);
    pthread_join(guide_id, NULL);
    printf("Guide is finished\n");
    return 0;
}
