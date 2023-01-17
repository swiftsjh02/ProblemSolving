import pprint
import sys

sys.setrecursionlimit(10000)



n,m=map(int,input().split())
max=0
tmp=0
def dfs_R(x,y):
    global max
    global tmp
    if x>=n or x <=-1 or y<=-1 or y>=m:
        return False

    if visited[x][y]==False and graph[x][y]==1:
        visited[x][y]=True
        tmp+=1
        dfs_R(x-1,y)
        dfs_R(x,y-1)
        dfs_R(x+1,y)
        dfs_R(x,y+1)
        return True
    return False
    
    

graph=[]
cnt=0

for i in range(n):
    temp=list(map(int,input().split()))
    graph.append(temp)
visited=[[False for i in range(m)]for i in range(n)]

for i in range(n):
    for j in range(m):
       if visited[i][j]==False:
        if(dfs_R(i,j)==True):
            if tmp>max:
                max=tmp
            tmp=0
            cnt+=1
        



print(cnt)
print(max)