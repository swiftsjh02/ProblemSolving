
x=int(input())

arr= list(map(int,input().split()))

dp=[1 for i in range(x)]

for i in range(1,x):
    for j in range(0,i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))


