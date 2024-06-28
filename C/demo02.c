#include <stdio.h>
#include <conio.h>

int main(int argc, char *argv[]) {
    int var=0;
    printf("Enter the number of which table you want : ");
    scanf("%d", &var);
    for (int i=1; i<=10; i++) {
        printf("%d x %d = %d\n", var, i, var*i);
    }
    printf("Program End.\n");

    return 0;
}
