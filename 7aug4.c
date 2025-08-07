#include<stdio.h>
int main(){
    int n1,n2,n3,n4;
    scanf("%d", &n1);
    scanf("%d", &n2);
    scanf("%d", &n3);
    scanf("%d", &n4);
    n1 = n1-50;
    n2 = n2-50;
    n3 = n3-50;
    n4 = n4-50;

    printf("%c %c %c %c\n", n1, n2, n3, n4);
}