#include <stdio.h>

typedef unsigned long long ull;

// Function to calculate Fibonacci numbers up to n using dynamic programming
void fibonacci(int n, ull* fib) {
    fib[0] = 1;
    fib[1] = 1;
    for (int i = 2; i <= n; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
}

ull perimeter(int n) {
    ull res = 0;
    ull fib[n + 1];
    fibonacci(n, fib);
    for (int i = 0; i <= n; ++i) {
        res += fib[i];
    }
    return 4 * res;
}

int main() {
    int n = 5; // Example value
    printf("Perimeter: %llu\n", perimeter(n));
    return 0;
}
