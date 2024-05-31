def permutations(s):
    # Initialize an empty list to store permutations
    result = []
 
    if len(s) == 1:
        return [s]
 
    for i in range(len(s)):
        current_char = s[i]
        remaining_chars = s[:i] + s[i+1:]
        for perm in permutations(remaining_chars):
            result.append(current_char + perm)
    return sorted(set(result))

s = "ssdd"
print(permutations(s))
