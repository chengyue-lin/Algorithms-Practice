from collections import Counter

s = raw_input()
letters = list(set(list(s)))
letters.sort()
counter = {x: y/2 for x, y in Counter(s).iteritems()}
A = ''
for i in xrange(len(s) - 1, -1, -1):
    x = s[i]
    c = s[i-1::-1].count(x)
    if c < counter[x]:
        A += x
        counter[x] -= 1
    elif x == letters[0]:
        A += x
        counter[x] -= 1
        if counter[x] == 0:
            letters.pop(0)
    else:
print A