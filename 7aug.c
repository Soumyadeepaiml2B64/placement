#include<stdio.h>
int carry(int num1, int num2) {
    int count = 0, carry = 0;
    if (num1 < 0 || num2 < 0) {
        return -1;
    }
    while (num1 > 0 || num2 > 0) {
        int d1 = num1 % 10;
        int d2 = num2 % 10;
        if (d1 + d2 + carry >= 10) {
            count++;
            carry = 1;
        } else {
            carry = 0;
        }
        num1 /= 10;
        num2 /= 10;
    }
    return count;
}

int main(){
    int m = carry(123,589);
    printf("%d\n", m);
    return 0;
}