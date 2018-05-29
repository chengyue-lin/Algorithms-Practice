#meetings =[(900, 1000), (930, 1030), (1000, 1100), (1030, 1130)]
meetings = [(900, 910), (940, 1200), (950, 1120), (1100, 1130), (1500, 1900), (1800, 2000)]

def sort_meetings(meetings):
    return sorted([x for x,_ in meetings]), sorted([x for _,x in meetings])


def num_rooms(arr, dep):
    platforms = 1
    result = 1

    i , j = 1, 0

    n = len(arr)

    while (i < n and j < n):

        if (arr[i] < dep[j]):
            platforms += 1
            i += 1

        else:
            platforms -= 1
            j += 1
        if (platforms > result):
            result = platforms
    return result

arr, dep = sort_meetings(meetings)

print(num_rooms(arr, dep))
