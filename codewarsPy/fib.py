
# def fib(n):
#   if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
#   a = b = x = 1
#   c = y = 0
#   while n:
#     if n % 2 == 0:
#       (a, b, c) = (a * a + b * b,
#                    a * b + b * c,
#                    b * b + c * c)
#       n /= 2
#     else:
#       (x, y) = (a * x + b * y,
#                 b * x + c * y)
#       n -= 1
#   return y
# def fib(n):
#     def fib_pair(k):
#         if k == 0:
#             return (0, 1)
#         else:
#             a, b = fib_pair(k // 2)
#             c = a * ((b << 1) - a)
#             d = a * a + b * b
#             if k & 1:
#                 return (d, c + d)
#             else:
#                 return (c, d)
    
#     if n == 0:
#         return 0
#     elif n < 0:
#         if n % 2 == 0:
#             return -fib_pair(-n)[0]
#         else:
#             return fib_pair(-n)[0]
#     else:
#         return fib_pair(n)[0]

# # Testing with a large number
# print(fib(1320643))




def fib(n):
    if n == 0:
        return 0
    sign = 1
    if n < 0:
        sign = -1 if n % 2 == 0 else 1
        n = -n
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b
    return b * sign if n > 1 else sign


print(fib(-1))