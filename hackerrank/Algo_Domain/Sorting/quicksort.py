def quickSort(ar):
    if len(ar) <= 1:
        return ar
    pivot = ar[0]
    l = [x for x in ar if x < pivot]
    r = [x for x in ar[1:] if x >= pivot]
    arr = quickSort(l) + [pivot] + quickSort(r)
    print " ".join(map(str, arr))
    return arr

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)