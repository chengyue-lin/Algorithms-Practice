from collections import Counter
def lonelyinteger(a):
	count = Counter(a)
    answer = min(count, key=count.get)
    return answer

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)