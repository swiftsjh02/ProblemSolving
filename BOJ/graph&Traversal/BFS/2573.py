import sys
sys.setrecursionlimit(100000)
from pprint import pprint
from collections import deque

n,m=map(int,input().split())
q=deque()
day=0
check=False

def bfs(y,x):
    q.append((y,x))
    while q:
        y,x=q.popleft()
        visit[y][x]=True

        
        if 0<=x-1<m and 0<=y<n:
            if a[y][x-1]!=0 and visit[y][x-1]==False:
                visit[y][x-1]=True
                q.append((y,x-1))
            elif a[y][x-1]==0:
                count[y][x]+=1
        if 0<=x+1<m and 0<=y<n:
            if a[y][x+1]!=0 and visit[y][x+1]==False:
                visit[y][x+1]=True
                q.append((y,x+1))
            elif a[y][x+1]==0:
                count[y][x]+=1
        if 0<=x<m and 0<=y+1<n:
            if a[y+1][x]!=0 and visit[y+1][x]==False:
                visit[y+1][x]=True
                q.append((y+1,x))
            elif a[y+1][x]==0:
                count[y][x]+=1
        if 0<=x<m and 0<=y-1<n:
            if a[y-1][x]!=0 and visit[y-1][x]==False:
                visit[y-1][x]=True
                q.append((y-1,x))
            elif a[y-1][x]==0:
                count[y][x]+=1
    return 1
    

a=[]

for i in range(n):
    tmp=list(map(int,input().split()))
    a.append(tmp)

        
    

cnt=0
while True:
    result=[]
    visit=[[False for i in range(m)] for i in range(n)] 
    count=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j]!=0 and visit[i][j]==False:
                result.append(bfs(i,j))
                
    
    for i in range(n):
        for j in range(m):
            a[i][j]=a[i][j] -count[i][j]
            if a[i][j]<0:
                a[i][j]=0
    if len(result)==0:
        break
    if len(result)>=2:
        check = True
        break
    day+=1

if check:
    print(day)
else:
    print(0)

   
                
    
    




   
