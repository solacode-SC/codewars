


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

def find_primes(num):
    abs_num = abs(num)
    output_set = set()
    if abs_num < 2:
        return []
    for i in range(2, int(abs_num ** 0.5) + 1):
        while abs_num % i == 0:
            output_set.add(i)
            abs_num //= i
    if abs_num > 1:
        output_set.add(abs_num)
    return list(output_set)

def fix_dup(lst):
    result = []
    for i in range(len(lst)):
        found = False
        for j in range(len(result)):
            if lst[i][0] == result[j][0]:
                result[j][1] += lst[i][1]
                found = True
                break
        if not found:
            result.append(lst[i])
    return sorted(result)

def sum_for_list(lst):
    outputArray = []
    for num in lst:
        if is_prime(num):
            outputArray.append([num, num])
        else:
            factors = find_primes(num)
            for factor in factors:
                outputArray.append([factor, num])
    return fix_dup(outputArray)






# def is_prime(num):
#     if num < 0:
#         num = -num
#     elif num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):  
#         if num % i == 0:
#             return False
#     return True

# def find_primes(num):
#     outputArray = []
#     if (num < 0):
#         num = -num
#     for i in range(2, num):  
#         if is_prime(i) and num % i == 0:
#             outputArray.append(i)
#     return outputArray
# def fix_dup(lst):
#     result = []
#     for i in range(len(lst)):
#         found = False
#         for j in range(len(result)):
#             if lst[i][0] == result[j][0]:
#                 result[j][1] += lst[i][1]
#                 found = True
#                 break
#         if not found:
#             result.append(lst[i])
#     return sorted(result)
# def sum_for_list(lst):
#     outputArray = []
#     for num in lst:
#         if is_prime(num):
#             outputArray.append([num, num])
#         else:
#             factors = find_primes(num)
#             for factor in factors:
#                 outputArray.append([factor, num])
#     print(outputArray)
#     return fix_dup(outputArray)

# list = [15, 30, -45, 13] 
# # print(sorted(sum_for_list(list)))
# lst = sum_for_list(list)
# print(lst)

