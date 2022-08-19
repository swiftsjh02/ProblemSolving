n=int(input())
a=[]
for i in range(n):
    b=[int(j) for j in input().split(" ")]
    a.append(b)
a.sort()

for x,y in a:
    print(x,y)

