def pairs(a, k):
    a.sort()
    answer = 0
    i, j = 0, len(a) - 1
    while i < len(a):
    	while (a[j] - a[i]) > k and j > 0: 
    		j-=1
    	while (a[j] - a[i]) < k and j < len(a) - 1:
    		j+=1
    	if (a[j] - a[i]) == k:
    		answer += 1
    	i += 1
    return answer

if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)