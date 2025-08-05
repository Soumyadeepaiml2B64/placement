#include<stdio.h>
int main(){
    int arr[6]={1,2,3,4,5,6};
    int key = 7;
    for (int i = 0; i < (key+1)/2; i++) {
        int temp = arr[i];
        arr[i] = arr[key - i];
        arr[key - i] = temp;
    }
    for (int i = 0; i < 6; i++) {
        printf("%d", arr[i]);
    }
    return 0;
}