#include <stdio.h>

int won(char b[3][3], char p) {
    for (int i = 0; i < 3; i++)
        if ((b[i][0] == p && b[i][1] == p && b[i][2] == p) || 
            (b[0][i] == p && b[1][i] == p && b[2][i] == p))
            return 1;

    return (b[0][0] == p && b[1][1] == p && b[2][2] == p) ||
           (b[0][2] == p && b[1][1] == p && b[2][0] == p);
}

int main() {
    char b[3][3];
    for (int i = 0; i < 3; i++)
        scanf(" %c %c %c", &b[i][0], &b[i][1], &b[i][2]);

    if (won(b, 'X'))
        printf("X is the winner\n");
    else if (won(b, 'O'))
        printf("O is the winner\n");
    else
        printf("Draw\n");

    return 0;
}
