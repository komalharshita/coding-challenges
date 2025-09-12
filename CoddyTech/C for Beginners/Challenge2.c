#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);

    printf("num = %d", num);

    int n1;
    int n2;
    scanf("%d %d", &n1, &n2);
    
    int n3 = n1 + n2;
    printf("%d", n3);
    
    return 0;
};