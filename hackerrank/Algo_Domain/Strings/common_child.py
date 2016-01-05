import time

s1, s2 = raw_input().strip(), raw_input().strip()
t1 = time.time()
l1, l2 = len(s1), len(s2)
count = 0

start_1 = 0
# start_2 = 0
end_1 = l1 - 1
end_2 = l2 - 1
while start_1 < l1 and start_1 < l2 and s1[start_1] == s2[start_1]:
    start_1 += 1
    count+= 1

while end_1 > 0 and end_2 > 0 and s1[end_1] == s2[end_2]:
    end_1 -= 1
    end_2 -= 1
    count += 1

x = [[0 for __ in xrange(start_1, end_2 + 2)] for __ in xrange(start_1, end_2 + 2)]
max_ = 0


for i in xrange(end_1 - start_1 + 1):
    for j in xrange(end_2 - start_1 + 1):
        if s1[i] == s2[j]:
            x[i + 1][j + 1] = x[i][j] + 1
        else:
            x[i + 1][j + 1] = max(x[i][j + 1], x[i + 1][j])
        if max_ < x[i + 1][j + 1]:
            max_ = x[i + 1][j + 1]

print max_ + count 
print time.time() - t1