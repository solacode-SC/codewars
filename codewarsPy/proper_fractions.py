# import math

# def is_prime(num):
#     if num < 2:
#         return False
#     if num in (2, 3):
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     for i in range(5, int(num ** 0.5) + 1, 6):
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#     return True

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def proper_fractions(n):
#     if n == 1:
#         return 0

#     result = n
#     p = 2
#     while p * p <= n:
#         if n % p == 0:
#             while n % p == 0:
#                 n //= p
#             result -= result // p
#         p += 1
#     if n > 1:
#         result -= result // n
    
    # return result













def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_common(a, b):
    for i in range (2, b + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True
def proper_fractions(n):
    result = 0
    if (n == 1):
        return 0
    elif is_prime(n) == True:
        return n - 1
    else:
        for i in range (1, n):
            # print(i)
            if is_prime(i) == True and n % i != 0:
                print(i, "*")
                result += 1
            elif find_common(n, i) == True:
                print(i, "&")
                result += 1
            else:
                print(i, "?")
                result += 0
    return result


a = 15

print(proper_fractions(a))
    