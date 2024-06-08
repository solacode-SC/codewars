def next_bigger(n):
    digits = list(str(n))
    length = len(digits)

    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1

    pivot = i

    for j in range(length - 1, pivot, -1):
        if digits[j] > digits[pivot]:
            break

    digits[pivot], digits[j] = digits[j], digits[pivot]

    digits = digits[:pivot + 1] + sorted(digits[pivot + 1:])

    result = int(''.join(digits))

    return result if result > n else -1


print(next_bigger(1045)) 