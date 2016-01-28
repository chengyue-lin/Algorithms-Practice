def calculate_n(arr, n):
    for i in xrange(2, n):
        arr.append(arr[i - 1]**2 + arr[i - 2])
    return arr[n-1]

def main():
    arr = []
    arr = map(int, raw_input().split())
    print calculate_n(arr, arr.pop(-1))

if __name__ == "__main__":
    main()