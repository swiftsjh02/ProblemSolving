
import pprint


n=int(input())
e=int(input())
arr=[[float('inf') for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            arr[i][j]=0
input=[list(map(int,input().split())) for i in range(e)]

for e in input:
    arr[e[0]-1][e[1]-1]=min(e[2],arr[e[0]-1][e[1]-1])



for l in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            arr[i][j]=min(arr[i][j],arr[i][l]+arr[l][j])

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]==float('inf'):
            print(0,end=' ')
        else:
            print(arr[i][j],end=' ')
    print()



