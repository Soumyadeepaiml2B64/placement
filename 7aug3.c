#include<stdio.h>
int main(){
    int sum =0;
    int n =10;
    int m= 15;
    for (int i=n;i<=m+1;i++){
        if(i%3==0 && i%5==0){
            sum+=i;
        }
    }
    printf("%d",sum);
    return 0;
}