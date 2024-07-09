#include <stddef.h>

// do not allocate memory for the output array
// assign values to preallocated array results

int get_smaller(size_t len,const int array[len], int num, int index) {
    int i = index;
    int k = 0;
    while (i < len) {
        if (num > array[i])
            k++;
        i++;
    }
    return k;
}

void smaller(size_t length, const int array[length], size_t results[length]) {
    int i = 0;
    while (i < length) {
        results[i] = get_smaller(length, array, array[i], i);
        i++;
    }
}

#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3};
    size_t len = sizeof(arr) / sizeof(arr[0]);
    size_t results[len];

    smaller(len, arr, results);

    for (size_t i = 0; i < len; i++) {
        printf("%zu: %zu\n", arr[i], results[i]);
    }

    return 0;
}