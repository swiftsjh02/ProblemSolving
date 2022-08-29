from collections import deque
import sys


def bfs(r):
    global cnt
    visit[r]=cnt
    cnt+=1
    queue.append(r)
    while len(queue)!=0:
        tmp=queue.popleft()
        for e in node[tmp]:
            if visit[e]==0:
                queue.append(e)
                visit[e]=cnt
                cnt+=1
            
    

cnt=1
n,m,r=map(int,input().split())
node=[[]*1 for i in range(n+1)]
queue=deque()
visit=[0]*(n+1)
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)



for i in range(1,n+1):
    node[i].sort(reverse=True)


bfs(r)

for i in range(1,n+1):
    print(visit[i])