n = int(raw_input())
arr = map(int, raw_input().strip().split())
while len(arr):
    item = min(arr)
    print len(arr)
    arr = [x for x in arr if item != x]