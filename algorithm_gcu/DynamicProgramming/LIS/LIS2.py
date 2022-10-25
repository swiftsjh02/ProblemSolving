input=list(map(int,input().split()))
dp=[1 for i in range(len(input))]

for i in range(len(input)):
    for j in range(i):
        if input[i]>input[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))