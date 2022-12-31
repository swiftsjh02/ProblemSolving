from pprint import pprint
from collections import deque

def tomato1(n,m,h):
    visited=[[[False for i in range(n)] for j in range(h)] for i in range(m)]

    count=0
    oneidx=deque()
    for i in range(m):
        for j in range(n):
            for k in range(h):
                if tomato[i][k][j]==1 and visited[i][k][j]==False:
                    oneidx.append((i,k,j))   

    


    tmp=get_one_idx(visited,oneidx,n,m,h)
    while len(tmp)!=0:
        tmp=get_one_idx(visited,tmp,n,m,h)
        count+=1

    zero=False
    for i in range(m):
        for j in range(n):
            for k in range(h):
                if tomato[i][k][j]==0:
                    zero=True
    if zero==True:
        print("-1")
    else:
        print(count)
                
                
        
    
       
        
                
def get_one_idx(visited,oneidx,n,m,h):
    tmp=deque()
    while len(oneidx)!=0:
            y,z,x=oneidx.popleft()
            visited[y][z][x]=True
            if 0<=y<m and 0<=x+1<n:
                if visited[y][z][x+1]==False and tomato[y][z][x+1]==0:
                    tomato[y][z][x+1]=1
                    tmp.append((y,z,x+1))
            if 0<=y<m and 0<=x-1<n:
                if visited[y][z][x-1]==False and tomato[y][z][x-1]==0:
                    tomato[y][z][x-1]=1
                    tmp.append((y,z,x-1))
            if 0<=y+1<m and 0<=x<n:
                if visited[y+1][z][x]==False and tomato[y+1][z][x]==0:
                    tomato[y+1][z][x]=1
                    tmp.append((y+1,z,x))
            if 0<=y-1<m and 0<=x<n:
                if visited[y-1][z][x]==False and tomato[y-1][z][x]==0:
                    tomato[y-1][z][x]=1
                    tmp.append((y-1,z,x))
            if 0<=y<m and 0<=x<n and 0<=z-1<h:
                if visited[y][z-1][x]==False and tomato[y][z-1][x]==0:
                    tomato[y][z-1][x]=1
                    tmp.append((y,z-1,x))
            if 0<=y<m and 0<=x<n and 0<=z+1<h:
                if visited[y][z+1][x]==False and tomato[y][z+1][x]==0:
                    tomato[y][z+1][x]=1
                    tmp.append((y,z+1,x))
    return tmp






n,m,h=map(int,input().split())
tomato=[[]for i in range(m)]
for i in range(m*h):
    tmp=list(map(int,input().split()))
    tomato[i%m].append(tmp)





tomato1(n,m,h)


