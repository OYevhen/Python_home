def non_recursive(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def recursive(n):
    if n == 0:
        return 1
    else:
        return n * recursive(n - 1)

print(non_recursive(5))
print(recursive(5))