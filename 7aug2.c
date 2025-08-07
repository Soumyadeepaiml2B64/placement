#include <stdio.h>
int is_palindrome(int n) {
    int rev = 0, temp = n;
    while (temp > 0) {
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }
    return n == rev;
}

int main() {
    int l, u;
    scanf("%d", &l);
    scanf("%d", &u);
    for (int i = l; i <= u; i++) {
        if (is_palindrome(i)) {
            printf("%d\n", i);
        }
    }
    return 0;
}