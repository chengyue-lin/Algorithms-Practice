def get_max(arr):
    res = []
    maximum = 0
    for idx, val in enumerate(arr):
        if arr[maximum] < val:
            maximum = idx
        res.append(maximum)
    return res

def get_max2(arr):
    res = [0] * len(arr)
    maximum = len(arr) - 1
    for idx in xrange(len(arr) - 1, -1, -1):
        if arr[maximum] < arr[idx]:
            maximum = idx
        res[idx] = maximum
    return res

def amount_water(input):
    length = len(input)
    water = 0
    max1_map = get_max(input)
    print "max1_map:", max1_map
    max2_map = get_max2(input)
    print "max2_map:", max2_map
    for index, height in enumerate(input):
        max1 = input[max1_map[index]]
        max2 = input[max2_map[index]]
        minimum = min(max1, max2)
        if minimum > height:
            water += (minimum - height)
    return water

if __name__ == "__main__":
    print amount_water([3, 0, 0, 2, 0, 4])
    print amount_water([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0])
    print amount_water([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0])
    print amount_water([3,1,4,0,0,6,0,3,0,2])
