#include <stdio.h>

int main() {
    int a = 3;
    int b = 2;

    if (a >= b) {
        printf("You are here!");
    }

    int age;
    scanf("%d", &age);
    if (age > 18) {
        printf("Above 18");
    }
    else {
        printf("Below or equal 18");
    }

    for (int i = 1; i <= 10; i++) {
        printf("hello\n");
    }

    
    return 0;
};