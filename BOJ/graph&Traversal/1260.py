import sys
from collections import deque


def dfs(r): 
    visited[r]=True
    print(r,end=" ")
    for e in node[r]:
        if visited[e]==False:
            dfs(e)

def bfs(r):
    visit[r]=True
    queue.append(r)
    while len(queue)!=0:
        tmp=queue.popleft()
        print(tmp,end=" ")
        for e in node[tmp]:
            if visit[e]==False:
                queue.append(e)
                visit[e]=True
                
    

n,m,r=map(int,input().split())



visited=[False]*(n+1)
node=[[]*n for k in range(n+1)]
visit=[False]*(n+1)
queue=deque()


for z in range(m):
    com=list(map(int,sys.stdin.readline().split()))
    node[com[0]].append(com[1])
    node[com[1]].append(com[0])

for i in range(n+1):
    node[i].sort()
    


    
dfs(r)
print()
bfs(r)

