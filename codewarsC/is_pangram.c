#include <stdbool.h>
#include <ctype.h>

bool is_pangram(const char *str_in) {
    bool seen[26] = {false};
    int index;
    
    for (int i = 0; str_in[i] != '\0'; i++) {
        if (isalpha(str_in[i])) {
            index = tolower(str_in[i]) - 'a';
            seen[index] = true;
        }
    }
    
    for (int i = 0; i < 26; i++) {
        if (!seen[i]) {
            return false;
        }
    }
    
    return true;
}


// #include <stdbool.h>

// bool is_pangram(const char *str_in) {
//   for (char x = 'a'; x <= 'z'; x++) if (!strchr(str_in, x) && !strchr(str_in, x - 'a' + 'A')) return false;
//   return true;
// }