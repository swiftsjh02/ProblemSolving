import math
n=int(input())

dp=[0 for i in range(max(n+1,3))]
dp[0]=1
dp[1]=1
dp[2]=2


for i in range(3,n+1):
    for j in range(0,i):
        dp[i]+=dp[j]*dp[i-j-1]

print(dp[n])

