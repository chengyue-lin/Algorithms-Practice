from sys import stdin

def lcs(s1, s2):
    dp_current = []
    dp_prev = []
    n, m = len(s1), len(s2)
    for __ in xrange(n+1):
        dp_current.append(0)
        dp_prev.append(0)
    for i in xrange(n + 1):
        for j in xrange(m + 1):
            if i == 0 or j == 0:
                dp_current[j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp_current[j] = dp_prev[j - 1] + 1
            else:
                dp_current[j] = max(dp_current[j-1], dp_prev[j])

        for j in xrange(n):
            dp_prev[j] = dp_current[j]
    return dp_current[-1]
                
def main():
    s, t = stdin.next().strip(), stdin.next().strip()
    print lcs(s, t)

main()