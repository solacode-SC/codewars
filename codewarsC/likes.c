#include <stdlib.h>
#include <string.h>
#include <stdio.h>

// Helper function to allocate and format a string
char *format_string(const char *format, ...) {
    va_list args;
    va_start(args, format);
    // Determine the length of the formatted string
    int len = vsnprintf(NULL, 0, format, args);
    va_end(args);
    
    // Allocate memory for the string
    char *str = (char *)malloc((len + 1) * sizeof(char));
    if (!str) {
        return NULL;
    }
    
    // Write the formatted string to the allocated memory
    va_start(args, format);
    vsnprintf(str, len + 1, format, args);
    va_end(args);
    
    return str;
}

char *one_likes(const char *name) {
    return format_string("%s likes this", name);
}

char *two_like(const char *name1, const char *name2) {
    return format_string("%s and %s like this", name1, name2);
}

char *three_like(const char *name1, const char *name2, const char *name3) {
    return format_string("%s, %s and %s like this", name1, name2, name3);
}

char *more_like(const char *name1, const char *name2, int count) {
    return format_string("%s, %s and %d others like this", name1, name2, count);
}

char *likes(size_t n, const char *const names[n]) {
    switch (n) {
        case 0:
            return format_string("no one likes this");
        case 1:
            return one_likes(names[0]);
        case 2:
            return two_like(names[0], names[1]);
        case 3:
            return three_like(names[0], names[1], names[2]);
        default:
            return more_like(names[0], names[1], n - 2);
    }
}


// #include <stdlib.h>
// #include <stddef.h>
// #include <string.h>
// #include <stdio.h>

// char* likes(size_t n, const char *const names[n]) {
//   char *buf;
//   switch (n) {
//     case 0:  { asprintf(&buf, "no one likes this"); break; }
//     case 1:  { asprintf(&buf, "%s likes this", names[0]); break; }
//     case 2:  { asprintf(&buf, "%s and %s like this", names[0], names[1]); break; }
//     case 3:  { asprintf(&buf, "%s, %s and %s like this", names[0], names[1], names[2]); break; }
//     default: { asprintf(&buf, "%s, %s and %d others like this", names[0], names[1], n-2); break; }
//   }
//   return buf;
// }