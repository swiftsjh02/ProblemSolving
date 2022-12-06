import pprint
import sys

sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n,m=map(int,input().split())
graph=[]
cnt=0
for i in range(n):
    temp=[0 for i in range(n)]
    graph.append(temp)
visited=[False for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u-1][v-1]=1
    graph[v-1][u-1]=1

pprint.pprint(graph)

for i in range(n):
    if visited[i]==False:
        dfs(graph,i,visited)
        cnt+=1







