def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)  # Sorting the numbers in ascending order
    return sorted_numbers[0] + sorted_numbers[1]  # Returning the sum of the two smallest numbers

array = [123, 45, 56, 34, 67, 323, 23]

print(sum_two_smallest_numbers(array))
