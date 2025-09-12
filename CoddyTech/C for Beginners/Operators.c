#include <stdio.h>

int main() {
    float a = 5;
    float b = 2;
    float c = a / b;
    
    printf("a = %2.1f, b = %2.1f, c = %2.1f", a, b, c);

    int count = 0;
    count++;
    count++;
    printf("count = %d", count);

    int n1 = 8;
    int n2 = 9;
    int n3 = n1 == n2;
    printf("n1 = %d, n2 = %d, n3 = %d", n1, n2, n3);

    int b1 = 1;
    int b2 = 1;
    int b3 = b1 && b2;
    printf("b3 = %d", b3);

    return 0;
};