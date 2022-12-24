n=int(input()) #target number 

dp = [0] * (n + 1) # table which save number of calculation to make index of array to 1

for i in range(2,n+1): 
    dp[i]=dp[i-1]+1

    if i%3==0:
        dp[i]=min(dp[i],dp[i//3] +1)
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
print(dp[n])
    