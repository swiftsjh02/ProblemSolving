from collections import deque

f,s,g,u,d=map(int,input().split())
visit=[False for i in range(f+1)]

def bfs(start):
    q=deque()
    q.append((start,0))
    while q:
        cur,cnt=q.popleft()
        if cur==g:
            return cnt
        if visit[cur]==False:
            visit[cur]=True
        else:
            continue

        if 0<cur-d<=f:
            q.append((cur-d,cnt+1))
        if 0<cur+u<=f:
            q.append((cur+u,cnt+1))
    return -1

result=bfs(s)
if result==-1:
    print("use the stairs")
else:
    print(result)