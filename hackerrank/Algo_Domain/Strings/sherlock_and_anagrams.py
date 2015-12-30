from collections import *
for i in range(input()):
    s = raw_input()
    check = defaultdict(int)
    l = len(s)
    for i in range(l):
        for j in range(i+1,l+1):
            sub = list(s[i:j])
            print sub
            sub.sort()
            sub = "".join(sub)
            check[sub]+=1
    sum = 0
    print check
    for i in check:
        n = check[i]
        sum += (n*(n-1))/2
    print sum