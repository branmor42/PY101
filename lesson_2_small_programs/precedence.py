def value(n):
    print(n)
    return n

print(value(3) + value(5) * value(7))

# a = b = c = 3
# 5 ** 3 ** 2  # 1953125 (same as 5 ** (3 ** 2) = 5 ** 9 = 5 * 5 * 5 * 5 * 5 * 5 * 5 * 5 * 5

# 5 and 1 / 0           # ZeroDivisionError
# None or 1 / 0         # ZeroDivisionError

print(None and 1 / 0)           # None
print(5 or 1 / 0)               # 5