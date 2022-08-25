n,k = map(int,input().split())
coins=[0]*n
for i in range(n):
    coins[n-i-1]=int(input())

count=0
for coin in coins:
    count=count+k//coin
    k=k%coin

print(count)

