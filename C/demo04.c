#include <stdio.h>
#include <conio.h>
#include "mylib.h"

int main(int argc, char *argv[]) {
    int num = 0;
    printf("Enter a int number : ");
    fflush(stdin); scanf("%d", &num);
    printf("The squire of number is %d .\n", num*num);
    printf("The actual int number is ");
    printInt(&num);
    printf("\n");

    float var = 5.6;
    printf("Enter a float number : ");
    fflush(stdin); scanf("%f", &var);
    printf("The squire of number is %.2f .\n", var*var);
    printf("The actual float number is ");
    printFloat(&var);

    return 0;
}

