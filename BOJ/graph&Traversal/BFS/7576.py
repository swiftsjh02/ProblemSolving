from pprint import pprint
from collections import deque

def tomato1(n,m):
    visited=[[False for i in range(n)] for j in range(m)]

    count=0
    oneidx=deque()
    for i in range(m):
        for j in range(n):
            if tomato[i][j]==1 and visited[i][j]==False:
                oneidx.append((i,j))        
    tmp=get_one_idx(visited,oneidx)
    while len(tmp)!=0:
        tmp=get_one_idx(visited,tmp)
        count+=1

    zero=False
    for i in range(m):
        for j in range(n):
            if tomato[i][j]==0:
                zero=True
    if zero==True:
        print("-1")
    else:
        print(count)
                
                
        
    
       
        
                
def get_one_idx(visited,oneidx):
    tmp=deque()
    while len(oneidx)!=0:
            y,x=oneidx.popleft()
            visited[y][x]=True
            if 0<=y<m and 0<=x+1<n:
                if visited[y][x+1]==False and tomato[y][x+1]==0:
                    tomato[y][x+1]=1
                    tmp.append((y,x+1))
            if 0<=y<m and 0<=x-1<n:
                if visited[y][x-1]==False and tomato[y][x-1]==0:
                    tomato[y][x-1]=1
                    tmp.append((y,x-1))
            if 0<=y+1<m and 0<=x<n:
                if visited[y+1][x]==False and tomato[y+1][x]==0:
                    tomato[y+1][x]=1
                    tmp.append((y+1,x))
            if 0<=y-1<m and 0<=x<n:
                if visited[y-1][x]==False and tomato[y-1][x]==0:
                    tomato[y-1][x]=1
                    tmp.append((y-1,x))
    return tmp






n,m=map(int,input().split())
tomato=[]
for i in range(m):
    tmp=list(map(int,input().split()))
    tomato.append(tmp)



tomato1(n,m)


