def fact(acc, n):
    return acc if n == 1 else fact(acc * n, n - 1)

n = int(raw_input().strip())
print fact(1, n)