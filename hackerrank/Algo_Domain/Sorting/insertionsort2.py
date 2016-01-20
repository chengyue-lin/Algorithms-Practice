def insertionSort(ar):  
    l = len(ar)
    for i in xrange(1, l):
        j = i - 1
        v = ar[i]
        while j >= 0 and v < ar[j]:
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = v
        print ' '.join(map(str, ar))
    return ar

__ = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)