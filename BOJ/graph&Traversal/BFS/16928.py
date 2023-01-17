from collections import deque
q=deque()
move=[0 for i in range(0,101)]
board=[i for i in range(0,101)]
visit=[False for i in range(0,101)]
def bfs(a):
    global cnt
    q.append(a)
    move[a]=[0,0]
    print(move)
    while q:
        
        tmp=q.popleft()
        if visit[tmp]==False:
            visit[tmp]=True
        else:
            continue
        if tmp==100:
            break
        for i in range(1,4,2):
            if tmp+i>100:
                break
            
            print(move)
            if lad.get(tmp+i)!=None:
                q.append(lad[tmp+i])    
                move[tmp+i]=[i,move[tmp][1]+1]
                if move[lad[tmp+i]]==0:
                    move[lad[tmp+i]]=[lad[tmp+i]-tmp-i,move[tmp+i][1]]
                else:
                    if move[tmp+i][1]+1<move[lad[tmp+i]][1]:
                        move[lad[tmp+i]]=[lad[tmp+i]-tmp-i,move[tmp+i][1]]
                    else:
                        continue
            elif snk.get(tmp+i)!=None:
                q.append(snk[tmp+i])
                move[tmp+i]=i
            else:
                q.append(tmp+i)
                move[tmp+i]=[i,move[tmp][1]+1]
                
        
        print(move)
            
        
    
    



n,m=map(int,input().split())
lad={}
lad_reverse={}
snk={}
snk_reverse={}
for i in range(n):
    a,b=map(int,input().split())
    lad[a]=b
for j in range(m):
    a,b=map(int,input().split())
    snk[a]=b


bfs(1)

print(move[100][1])