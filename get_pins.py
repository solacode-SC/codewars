
def get_pins(observed):
    keypad = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['8', '0']
    }

    observed_digits = list(observed)
    print(observed_digits)
    combinations = ['']

    for digit in observed_digits:
        new_combinations = []
        for combination in combinations:
            for possible_digit in keypad[digit]:
                new_combinations.append(combination + possible_digit)
        combinations = new_combinations

    return combinations


print(get_pins("125"))

# from itertools import product

# def reverse_sublists(input_list):
#     return [sublist[::-1] for sublist in input_list]
# def get_pins(observed):
#     adjacency_list = [[1, [1, 2, 4]],
#                       [2, [1, 2, 3, 5]],
#                       [3, [2, 3, 6]],
#                       [4, [1, 4, 5, 7]],
#                       [5, [2, 4, 5, 6, 8]],
#                       [6, [3, 5, 6, 9]],
#                       [7, [4, 7, 8]],
#                       [8, [5, 7, 8, 9, 0]],
#                       [9, [6, 8, 9]],
#                       [0, [8, 0]]]
    
#     result = []
#     intOb = int(observed)
    
#     if intOb < 10:
#         for item in adjacency_list:
#             if item[0] == intOb:
#                 for j in item[1]:
#                     result.append(str(j))
#         return result
#     else:
#         list1 = []
#         num = int(observed)
#         while num > 0:
#             for item in adjacency_list:
#                 if item[0] == num % 10:
#                     list2 = []
#                     for j in item[1]:
#                         list2.append(str(j))
#                     list1.append(list2)
#             num = num // 10
#         print(list1)
#         list5 = list(reversed(list1))
#         print(list5)
#         # Generate all possible combinations
#         possible_combinations = list(product(*list5))
        
#         # Join the combinations into strings
#         result = [''.join(p) for p in possible_combinations]
#         return result

# # Example usage
# observed_pin = "123"
# possible_pins = get_pins(observed_pin)
# print(possible_pins)


    