from collections import Counter

def isOneEdit(a, b):
    if abs(len(a) - len(b)) > 1: 
        return False
    freq = Counter()
    odd = 0
    def addOdds(arr, odd):
        for item in arr:
            freq[item] += 1
            if freq[item] % 2 == 1:
                odd += 1
            else:
                odd -= 1
        return odd
    
    odd = addOdds(a, odd)
    odd = addOdds(b, odd)
    return odd <= 2

if __name__ == "__main__":
    x = raw_input("Enter two strings:\n")
    a, b = x.split()
    print isOneEdit(a, b)
