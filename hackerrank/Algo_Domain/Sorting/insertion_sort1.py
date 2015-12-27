def insertionSort(ar):  
    V = ar[-1]
    l = len(ar)
    for i in xrange(l - 2, -1, -1):
        # print "i", i
        if V > ar[i]:
            ar[i + 1] = V
            print ' '.join(map(str, ar))
            return ar
        else:
            ar[i+1] = ar[i]
            print ' '.join(map(str, ar))
    ar[0] = V
    print ' '.join(map(str, ar))
    return ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)