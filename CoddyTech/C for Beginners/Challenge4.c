#include <stdio.h>

int main() {
    char op;
    float num1, num2;

    while (1) {
        // Try reading an operator
        if (scanf(" %c", &op) != 1) {
            break;
        }

        // Exit if 'e' is entered
        if (op == 'e') {
            break;
        }

        // Read the two numbers
        if (scanf("%f %f", &num1, &num2) != 2) {
            printf("Invalid input\n");
            break;
        }

        // Perform the operation
        switch (op) {
            case '+':
                printf("%f\n", num1 + num2);
                break;
            case '-':
                printf("%f\n", num1 - num2);
                break;
            case '*':
                printf("%f\n", num1 * num2);
                break;
            case '/':
                if (num2 != 0) {
                    printf("%f\n", num1 / num2);
                } else {
                    printf("Error: Division by zero\n");
                }
                break;
            default:
                printf("Invalid operator\n");
                break;
        }
    }

    return 0;
}
