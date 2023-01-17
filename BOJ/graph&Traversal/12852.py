from collections import deque
q=deque()
n=int(input())
visit=[False for i in range(n+1)]
history=[]
def bfs(k):
    q.append([1])

    while q:
        tmp=q.popleft()
        if visit[tmp[-1]]==False:
            visit[tmp[-1]]=True
        else:
            continue
        if tmp[-1]==k:
            return tmp

        if tmp[-1]*3<=k and visit[tmp[-1]*3]==False:
            q.append(tmp+[tmp[-1]*3])
            
        if tmp[-1]*2<=k and visit[tmp[-1]*2]==False:
            q.append(tmp+[tmp[-1]*2])
           
        if tmp[-1]+1<=k and visit[tmp[-1]+1]==False:
            q.append(tmp+[tmp[-1]+1])
    print(q)
    
    
    



result=bfs(n)
print(len(result)-1)
for i in range(len(result)-1,-1,-1):
    print(result[i],end=" ")





