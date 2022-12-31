from collections import deque
from pprint import pprint

def bfs(graph,start,visited):
    queue= deque()
    queue.append(start)
    visited[start]=True
    while len(queue)!=0:
        v=queue.popleft()
        print(v)
        for i in graph[v]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
    

v,e=map(int,input().split())
start=int(input())
visited=[False for i in range(v+1)]
graph=[[] for i in range(v+1)]
for i in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)


pprint(graph)

bfs(graph,start,visited)
