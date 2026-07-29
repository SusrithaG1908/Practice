def sumAndMultiply(n):
    digits=[int(c) for c in str(n) if c!='0']
    x = int(''.join(map(str, digits))) if digits else 0
    return x * sum(digits)

print(sumAndMultiply(10203004))