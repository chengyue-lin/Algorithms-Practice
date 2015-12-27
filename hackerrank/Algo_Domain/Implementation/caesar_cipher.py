def update(item, start, end):
    if ord(item) >= start and ord(item) <= end:
        element = ord(s[i]) + k
        while element > end:
            element = start + (element - end) - 1
        return chr(element)
    return item

n = int(raw_input().strip())
s = list(raw_input().strip())
k = int(raw_input().strip())
for i in xrange(n):
    s[i] = update(s[i], 97, 122)
    s[i] = update(s[i], 65, 90)
print "".join(s)