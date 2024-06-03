def decompose(n):
    def find_decomposition(remaining, current):
        if remaining == 0:
            return []
        
        for k in range(current - 1, 0, -1):
            if remaining - k**2 >= 0:
                result = find_decomposition(remaining - k**2, k)
                if result is not None:
                    return result + [k]
        
        return None
    
    return find_decomposition(n**2, n)

# Examples
print(decompose(11))  # Output: [1, 2, 4, 10]
print(decompose(50))  # Output: [1, 3, 5, 8, 49]
