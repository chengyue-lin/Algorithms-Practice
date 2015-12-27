def fact(acc, n):
    return acc * n if n == 2 else fact(acc * n, n - 1)

n = int(raw_input().strip())
print fact(1, n)