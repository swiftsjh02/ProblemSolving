from pprint import pprint
n=int(input())
triangle=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    triangle.append(tmp)



for i in range(1,n):
    for k in range(i+1):
        if k==0:
            triangle[i][k]+=triangle[i-1][k]
        elif k==i:
            triangle[i][-1]+=triangle[i-1][-1]
        else:
            triangle[i][k]+=max(triangle[i-1][k-1],triangle[i-1][k])

print(max(triangle[n-1]))
