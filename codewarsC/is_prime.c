#include <stdbool.h>

bool is_prime(int num) {
    if (num <= 1) {
        return false;
    } else if (num <= 3) {
        return true; // 2 and 3 are prime numbers
    } else if (num % 2 == 0 || num % 3 == 0) {
        return false; // multiples of 2 and 3 are not primes
    }

int i = 5;
while (i * i <= num) {
    if (num % i == 0 || num % (i + 2) == 0) {
        return false;
    }
    i += 6;
    }
    return true;
}
