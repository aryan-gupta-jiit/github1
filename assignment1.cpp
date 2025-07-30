#include <stdio.h>

int main() {
    int number, reversed;

    printf("Enter a 3-digit number: ");
    scanf("%d", &number);

    if (number < 100 || number > 999) {
        printf("Please enter a valid 3-digit number.\n");
        return 1;
    }

    int units = number % 10;
    int tens = (number / 10) % 10;
    int hundreds = number / 100;

    reversed = units * 100 + tens * 10 + hundreds;

    printf("Reversed number: %d\n", reversed);

    return 0;
}
