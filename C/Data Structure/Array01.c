/*
Implementation of various array operation.
1. Traversal : Processing each element in the array.
2. Search : Finding the location of an element with a given value.
3. Insertion : Adding a new element to an array.
4. Deletion : Removing an element from an array.
5. Sorting : Organizing the array elements in some order.
6. Merging : Combining two arrays into a single array.
7. Reversing : Reversing the elements of an array.
*/

#include <stdio.h>
#define MAX 5

void insert(int*, int pos, int num);
void del(int*, int pos);
void reverse(int*);
void display(int*);
void search(int*, int num);

////////////////////////////////////////////////////////////////////////////////////////////////
int main(int *argc, char *argv[]) {
    int arr[MAX];
    for(int i=0; i<MAX; i++)
        insert(arr, i+1, (i+1)*11);
    display(arr);
    del(arr, 3);
    display(arr);
    reverse(arr);
    display(arr);
    search(arr, 55);

    return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////

// =============================================================================================
void display(int *arr){
    printf("[");
    for(int i=0; i<MAX; i++){
        printf("%d", arr[i]);
        if (i!=MAX-1)
            printf(", ");
    }
    printf("]\n");
}

// =============================================================================================
void insert(int *arr, int pos, int num) {
    int i=0;
    for(i=MAX; i>=pos; i--)
        arr[i] = arr[i-1];
    arr[i] = num;
}

// =============================================================================================
void del(int *arr, int pos){
    int i=0;
    for (i=pos; i<MAX; i++){
        arr[i-1] = arr[i];
    }
    arr[i-1] = 0;
}

// =============================================================================================
void reverse(int *arr) {
    int i=0, temp=0;
    for (i=0; i<MAX/2; i++){
        temp = arr[i];
        arr[i] = arr[MAX-1-i];
        arr[MAX-1-i] = temp;
    }
}

// =============================================================================================
void search(int *arr, int num){
    int i=0;
    for(i=0; i<MAX; i++){
        if (arr[i] == num){
            printf("%d", i);
            return;
        }   
    }
    printf("Not Preset.\n");
}


