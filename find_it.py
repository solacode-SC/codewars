from collections import Counter

def find_it(seq):
    counts = Counter(seq)
    print(counts)
    for key, value in counts.items():
        if value % 2 != 0:
            return key
    return "No odd occurrences"

sequence = [2, 3, 45, 2, 45, 24, 54, 453, 3, 44]
result = find_it(sequence)
print(result)
