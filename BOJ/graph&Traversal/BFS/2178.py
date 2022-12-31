from pprint import pprint
from collections import deque

def tomato1(n,m):

    
    q=deque((0,0))
    

    while q:
        y,x=q.popleft()
        if 0<=y<m and 0<=x+1<n:
            if tomato[y][x+1]==1:
                tomato[y][x+1]=tomato[y][x]+1
                q.append((y,x+1))
        if 0<=y<m and 0<=x-1<n:
            if tomato[y][x-1]==1:
                tomato[y][x-1]=tomato[y][x]+1
                q.append((y,x-1))
        if 0<=y+1<m and 0<=x<n:
            if tomato[y+1][x]==1:
                tomato[y+1][x]=tomato[y][x]+1
                q.append((y+1,x))
        if 0<=y-1<m and 0<=x<n:
            if tomato[y-1][x]==1:
                tomato[y-1][x]=tomato[y][x]+1
                q.append((y-1,x))
            
        
     
    print(tomato[m-1][n-1])    

                
        
    
       
        

    
   






n,m=map(int,input().split())
tomato=[]
for i in range(m):
    tmp=list(map(int,input().split()))
    tomato.append(tmp)



tomato1(n,m)


