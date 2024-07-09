#include <stdbool.h>

typedef unsigned long long ull;




ull n_square(ull num, ull i) {
    if (i == 0)
        return 1;
    else {
        return num * n_square(num, i - 1);
    }
}

unsigned long long int sqrt_ull(unsigned long long int n) {
    if (n == 0 || n == 1) {
        return n;
    }

    unsigned long long int start = 1, end = n, mid, sqrt;

    while (start <= end) {
        mid = (start + end) / 2;

        if (mid * mid == n) {
            return mid;
        }

        if (mid * mid < n) {
            start = mid + 1;
            sqrt = mid;
        } else {
            end = mid - 1;
        }
    }

    return sqrt;
}

bool three_powers(ull n) {

    ull i, j, k;
    if (n <= 0) {
        return false;
    }
    i = 0;
    while (i < sqrt_ull(n)) {
        j = 0;
        while (j <= i) {
            k = 0;
            while (k <= j) {
                if (n == (n_square(2, i) + n_square(2, j) + n_square(2, k)))
                    return true;
                k++;
            }
            j++;
        }
        i++;
    }
    return false;
    
}
#include <stdio.h>

int main() {
    int n = 5;

    if (three_powers(n)) {
        printf("true");
    }
    else
    {
        printf("false %d \n", n_square(2,0));
    }
}