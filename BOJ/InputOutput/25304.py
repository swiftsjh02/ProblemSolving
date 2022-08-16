total=int(input())
n=int(input())

for i in range(n):
    a=[int(k) for k in input().split(" ")]
    total=total-a[0]*a[1]

if total==0:
    print("Yes")
else:
    print("No")