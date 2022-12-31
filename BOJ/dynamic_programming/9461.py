n=int(input())
for i in range(n):
    k=int(input())
    dp=[1 for i in range(k+1)]
    if k<4:
        print(dp[k])
        continue
    for j in range(4,k+1):
        dp[j]=dp[j-2]+dp[j-3]
    print(dp[k])

