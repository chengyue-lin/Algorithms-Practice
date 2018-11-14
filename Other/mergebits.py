def insert(N, M, i, j):
    allOnes = ~0
    left = allOnes << j
    right = (1 << i) - 1
    mask = left | right
    M = M << i
    N = N & mask
    return bin(N | M)

if __name__ == "__main__":
    print insert(int('10000000000', 2), int('10011', 2), 2, 6)
