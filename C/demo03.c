#include <stdio.h>
#include <conio.h>

int main(int argc, char *argv[]) {
	printf("Hello World\n");
	printf("Welcome to the world of Programming.\n");
	int var = 0;
	printf("Enter your age programmer : ");
	scanf("%d", &var);
	
	if (var >= 0 && var < 21)
		printf("Hey Hi, New Programmer. You are the young one, who is here.\n");
	else if (var >= 21 && var < 35)
		printf("Hello Programmer. You are expert in programming.\n");
	else if (var >= 35 && var < 100)
		printf("Hey Sir. You are the master of programming. Professional in programming.\n");
	else
		printf("Sorry Programmer. You must enter some invalid input.\n");
	
	return 0;
}
