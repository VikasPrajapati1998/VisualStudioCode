#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int main() {
    printf("Enter your favourite number : ");
    int var;
    fflush(stdin);
    scanf("%d", &var);

    printf("Hi Programmer. Your favourite number is %d.\n", var);

    return 0;
}

