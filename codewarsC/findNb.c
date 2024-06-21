#include <stdio.h>

long long findNb(long long m) {
    long long n = 0;
    long long volume = 0;

    while (volume < m) {
        n += 1;
        volume += n * n * n;
    }

    if (volume == m)
        return n;
    else
        return -1;
}

// Example usage
int main() {
    printf("%lld\n", findNb(1071225));         // Output: 45
    printf("%lld\n", findNb(91716553919377));  // Output: -1
    return 0;
}
