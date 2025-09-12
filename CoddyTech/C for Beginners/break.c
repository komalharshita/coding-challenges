#include <stdio.h>

int main() {
    for (int i = 0; i < 100; i += 3) {
        // Don't change above this line
        if (i > 21) {
            break;
        }
        printf("%d\n", i);
    }
    return 0;
};