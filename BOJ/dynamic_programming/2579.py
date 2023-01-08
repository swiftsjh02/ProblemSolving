n=int(input())
arr=[0]
for i in range(n):
    arr.append(int(input()))

dp=[0]*301

if n==1:
    print(arr[1])
elif n==2:
    print(arr[1]+arr[2])
else:
    dp[1]=arr[1]
    dp[2]=arr[1]+arr[2]
    dp[3]=max((arr[1]+arr[3]),arr[2]+arr[3])
    for i in range(4,n+1):
        dp[i]=max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
    print(dp[n])