t = int(raw_input())
for tc in xrange(t):
    ipt = raw_input().split()
    kkk = int(ipt[0])
    p = map(float, ipt[1:])
    dp = [[[0.0 for i in xrange(1001)] for j in xrange(kkk+1)] for k in xrange(kkk+1)]
    pu = int(p[3] * 1000)
    pd = int(p[5] * 1000)
    dp[0][0][int(p[2]*1000)] = 1.0
    for i in xrange(kkk):
        for j in xrange(kkk):
            for k in xrange(1001):
                pn = k / 1000.0
                dp[i+1][j][min(1000, k+pu)] += (p[0]*pn + p[1]*(1-pn))*p[4]*dp[i][j][k]; 
                dp[i+1][j][k] += (p[0]*pn + p[1]*(1-pn))*(1-p[4])*dp[i][j][k]; 
                dp[i][j+1][max(0, k-pd)] += ((1-p[0])*pn + (1-p[1])*(1-pn))*p[6]*dp[i][j][k]
                dp[i][j+1][k] += ((1-p[0])*pn + (1-p[1])*(1-pn))*(1-p[6])*dp[i][j][k]
    ans = 0.0
    for j in xrange(kkk):
        for k in xrange(1001):
            ans += dp[kkk][j][k]
    print "Case #%d: %.6f" % (tc + 1, ans)
