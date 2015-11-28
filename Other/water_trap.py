def amount_water(input):
    length = len(input)
    water = 0
    for index, height in enumerate(input):
        m1 = input[0: index]
        m2 = input[index + 1: ]
        max1, max2 = height, height
        if len(m1):
            max1 = max(m1)
        if len(m2):
            max2 = max(m2)
        minimum = min(max1, max2)
        if minimum > height:
            water += (minimum - height)
    return water

if __name__ == "__main__":
    print amount_water([3, 0, 0, 2, 0, 4])