n = int(raw_input())
arr = sorted(map(int, raw_input().strip().split()))
prev_item = arr[0]
print len(arr)
for index, item in enumerate(arr):
    if item != prev_item:
        print n - index
        prev_item = item