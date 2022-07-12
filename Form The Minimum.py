# Form The Minimum

def min_value(digits):
    return int(''.join(str(i) for i in sorted(list(set(digits)))))


print(min_value([1, 3, 1]))
