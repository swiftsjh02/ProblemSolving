n=int(input())




for i in range(n):
    temp=int(input())
    dp=[0 for i in range(temp+1+4)]
    dp[1]=1
    dp[2]=2
    dp[3]=4
    if temp<4:
        print(dp[temp])
        continue
    
    for i in range(4,temp+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

    print(dp[temp])

