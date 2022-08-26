n=int(input())

n=1000-n
count=0
coins=[500,100,50,10,5,1]

for coin in coins:
    count+=n//coin
    n=n%coin

print(count)

