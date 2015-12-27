t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    for __ in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    for __ in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
    i, j, k, l = 0, 0, 0, None
    answer = "NO"
    while i < R:
      # print "i", i, "j", j, "k", k, "l", l
      # print "P[j]", P[j], "G[i][k:l]", G[i][k:l]
      if P[j] in G[i][k:l]:
        k = G[i].index(P[j])
        l = k + c
        j += 1
      else:
        if j != 0:
          i = i - j + 1
        j = 0
        k = 0
      i+=1
      if j == (r):
        # print "j", j, "r", (r)
        answer = "YES"
        break
    print answer