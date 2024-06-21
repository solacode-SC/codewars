#include <stddef.h>

size_t str_count(const char *str, char letter) {
    int i = 0;
    size_t count = 0;
    while (str[i] != '\0') {
        if (str[i] == letter)
            count += 1;
        i++;
    }
    return count;
}
