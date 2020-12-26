
tour: tour.c
	gcc -Wall -g -o tour tour.c -lpthread


# The following test will check to see if there are any synchronization errors
# or race conditions in your code.  Do NOT spend time  trying to decipher 
# the output of helgrind

tester: tour
	@echo "WARNING: tester only works on teach.cs"
	@echo "Expected output: A line that contains the text \'0 errors\'"
	@echo "If the program hangs, then there is something wrong"
	valgrind --tool=helgrind ./tour 3 12 2>&1 | grep ERROR
