from pprint import pprint

def record(a,dp,x,y,sum):
    if x==n:
        return

    sum+=a[y][x]
    if dp[y][x]==0:
        dp[y][x]=sum
    else:
        dp[y][x]=min(dp[y][x],sum)

    record(a,dp,x+1,y,sum)
    record(a,dp,x+1,(y+1)%m,sum)
    record(a,dp,x+1,y-1,sum)

m,n=map(int,input().split())
a=[list(map(int,input().split())) for i in range(m)]
dp=[[0]*n for i in range(m)]
sum=0

pprint(a)
cost=float('inf')
record(a,dp,0,0,sum)


pprint(dp)

for i in range(m):
    cost=min(cost,dp[i][n-1])

print(cost)




