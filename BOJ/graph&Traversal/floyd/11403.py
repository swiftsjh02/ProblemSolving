import pprint
import math


n=int(input())
graph=[]
for i in range(n):
    temp=list(map(int,input().split()))
    graph.append(temp)

for i in range(n):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j]=float('inf')

pprint.pprint(graph)

for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
        


        


pprint.pprint(graph)




