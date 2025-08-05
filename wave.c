#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    char str[16] = ""; 
    char buf[4];

    for (int i = 0; i < 5; i++) {
        sprintf(buf, "%d", arr[i]);
        strcat(str, buf);
    }

    int num = atoi(str);
    num += 1;

    printf("%d\n", num);
    return 0;
}