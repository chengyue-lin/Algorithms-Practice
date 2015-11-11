def bin_search(arr, x):
    print arr
    l = len(arr)
    if x == arr[l/2]:
        return l/2
    if x > arr[l/2]:
        return l/2 + bin_search(arr[l/2:], x)
    else:
        return bin_search(arr[:l/2], x)
    
def insertionSort(ar):  
    V = ar[len(ar) - 1]
    l = len(ar)
    for i in reversed(xrange(l)):
        print i
        print ar
        if V < ar[i]:
            ar[i] = ar[i - 1]
        else:
            ar[i] = V
            print '%s' % ' '.join(map(str, ar))
            return ar
        print '%s' % ' '.join(map(str, ar))
    return ar

if __name__ == "__main__":
    # V = int(raw_input())
    # n = int(raw_input())
    # ar = map(int, raw_input().split())
    
    # print bin_search(ar, V)
    m = input()
    ar = [int(i) for i in raw_input().strip().split()]
    print insertionSort(ar)