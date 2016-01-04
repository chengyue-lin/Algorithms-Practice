from collections import Counter

s = raw_input()
letters = list(set(list(s)))
letters.sort()
counter = {x: y/2 for x, y in Counter(s).iteritems()}
A = ''
smallest_yet = chr(123)
for i in xrange(len(s) - 1, -1, -1):
    x = s[i]
    c = s[i-1::-1].count(x)
    print "smallest_yet", smallest_yet
    if smallest_yet > x and x in letters:
        smallest_yet = x
    print "\n"
    print s[i-1::-1]
    print x
    print letters
    print "c", c
    print "counter[",x,"]", counter[x]
    if c < counter[x]:
        A += smallest_yet
        smallest_yet = chr(123)
        counter[x] -= 1
    elif len(letters) and x == letters[0]:
        if counter[x] > 0:
            A += smallest_yet
            smallest_yet = chr(123)
            counter[x] -= 1
        print "counter after modification", counter[x]
    if counter[x] == 0 and x in letters:
        letters.remove(x)
    print "A is", A
print A