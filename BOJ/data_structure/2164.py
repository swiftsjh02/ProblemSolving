n=int(input())
a=[k for k in range(1,1000000)]
front=0
rear=n-1

for i in range(n-1):
    front+=1
    a[rear+1]=a[front]
    rear+=1
    front+=1


print(a[front])
