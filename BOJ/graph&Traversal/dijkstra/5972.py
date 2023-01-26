from collections import deque
from pprint import pprint
import heapq
import sys

def dijkstra(start):
    q=[]
    distance[start][0]=0
    heapq.heappush(q,[0,start])

    while q:
        dist,cur=heapq.heappop(q)
       
        for node,cost in graph[cur]:
            cost_new=cost+dist
            if cost_new<distance[node][k-1]:
                distance[node][k-1]=cost_new
                distance[node].sort()
                heapq.heappush(q,[cost_new,node])




        


n,m,k=map(int,input().split())
graph=[[] for i in range(n+1)]
distance=[[float('inf')]*k for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append([b,c])


dijkstra(1)
print(distance)
for i in range(1, n + 1):
    if distance[i][k-1] == float('inf'):
        print(-1)
    else:
        print(distance[i][k-1])
