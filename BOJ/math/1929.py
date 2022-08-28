n,m=map(int,input().split())

num=[0]*(m+1)

for i in range(2,m+1):
    num[i]=i



for i in range(2,m+1):
    if num[i]==0:
        continue

    for k in range(2*i,m+1,i):
        num[k]=0

for i in range(n,m+1):
    if num[i]!=0:
        print(num[i])