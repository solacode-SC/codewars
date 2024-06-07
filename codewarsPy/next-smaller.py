def next_smaller(n):
    digits = list(str(n))  
    length = len(digits)
    print(digits)
    for i in range(length - 2, -1, -1):
        if digits[i] > digits[i + 1]:
            break
    else:
        return -1 
    
    
    pivot = i
    for j in range(length - 1, pivot, -1):
        if digits[j] < digits[pivot]:
            break
    
    print(digits)
    digits[pivot], digits[j] = digits[j], digits[pivot]
    print(digits)
    digits = digits[:pivot + 1] + sorted(digits[pivot + 1:], reverse=True)
    print(digits)
    result = int(''.join(digits))
    if (length != len(list(str(result)))):
        return -1
    return result if result < n and str(result)[0] != '0' else -1


print(next_smaller(1001)) 
