import pprint
import math


n,m=map(int,input().split())
graph=[[float('inf') for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1





for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])
        

result=[0 for i in range(n+1)]
minidx=float('inf')
mind=float('inf')
for i in range(1,n+1):
    tmp=0
    for j in range(1,n+1):
        if i!=j:
            tmp+=graph[i][j]
    result[i]=tmp


for i in range(1,n+1):
    if mind>result[i]:
        mind=result[i]
for i in range(1,n+1):
    if result[i]==mind:
        minidx=min(i,minidx)
print(minidx)
