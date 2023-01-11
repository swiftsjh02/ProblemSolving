import sys


n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))


cnt=0
b=n
for i in range(n):
    sum=0
    for j in range(n-b+1):
        
        if n-b==0 or sum==0:
            for k in range(j,j+b):
                sum+=arr[k]
        else:
            sum=sum-arr[j-1]
            sum=sum+arr[j+b-1]

        if sum==m:
            cnt+=1
    
    b=b-1

print(cnt)

