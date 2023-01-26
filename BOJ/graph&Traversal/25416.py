from pprint import pprint
from collections import deque
def bfs(a,b):
    q=deque()
    q.append((a,b,0))

    while q:
        y,x,c=q.popleft()
        if y<0 or y>=5 or x<0 or x>=5:
            continue
        if graph[y][x]==-1:
            continue
        if graph[y][x]==1:
            print(c)
            return 1
        graph[y][x]=-1
    
        q.append((y,x+1,c+1))
        q.append((y,x-1,c+1))
        q.append((y+1,x,c+1))
        q.append((y-1,x,c+1))
    return -1



graph=[]
visit=[]
for i in range(5):
    graph.append(list(map(int,input().split())))


r,c=map(int,input().split())
if(bfs(r,c)==-1):
    print(-1)