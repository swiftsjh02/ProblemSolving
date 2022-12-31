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



for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])
        


        
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j]==float('inf'):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print("")




