import pprint
import sys

sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = True
    for i in range(len(graph[v])):
        if graph[v][i]==1 and visited[i]==False:
            dfs(i)
    return
    
    

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



for i in range(n):
    if visited[i]==False:
        dfs(i)
        cnt+=1

print(cnt)