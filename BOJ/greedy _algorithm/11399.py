n=int(input())

a=list(map(int,input().split()))
a.sort()
print(a)
total=0

for i in range(n):
    for j in range(0,i+1):
        total=total+a[j]

    

print(total)

