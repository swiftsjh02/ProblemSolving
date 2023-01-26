from collections import deque
num=int(input())
visit=[[-1 for j in range(num+1)] for i in range(num+1)]
visit[1][0]=0
def bfs():
    #stage={}
    q=deque()
    q.append((1,0))
    #stage[(1,0)]=0
    while q:
        x,clip=q.popleft()
   
        if x==num:
            #print(stage[(num,clip)])
            print(visit[x][clip])
            break
        # if (num,clip) in visit:
        #     continue
        # else:
        #     visit.add((num,clip))
        dx=[clip,0,-1]
        for i in range(3):
            nx =x+dx[i]
            if nx<0 or nx>num:
                continue
            if i==1 and visit[nx][x]==-1:
                q.append((nx,x))
                visit[nx][x]=visit[x][clip]+1
                #stage[(nx,num)]=stage[((num,clip))]+1
            if i!=1 and visit[nx][clip]==-1:
                q.append((nx,clip))
                visit[nx][clip]=visit[x][clip]+1
                #stage[(nx,clip)]=stage[(num,clip)]+1
        
     
bfs()