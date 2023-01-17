import sys
sys.setrecursionlimit(10**5)
n=int(input())
graph=[]
visit=[[False for i in range(n)] for k in range(n)]
visit2=[[False for i in range(n)] for k in range(n)]

for i in range(n):
    graph.append(list(input()))


def dfs_R(x,y):
    if x>=n or x <=-1 or y<=-1 or y>=n:
        return False

    if visit[x][y]==False and graph[x][y]=="R":
        visit[x][y]=True
        
        
        dfs_R(x-1,y)
        dfs_R(x,y-1)
        dfs_R(x+1,y)
        dfs_R(x,y+1)
        return True
    return False
def dfs_G(x,y):
    if x>=n or x <=-1 or y<=-1 or y>=n:
        return False

    if visit[x][y]==False and graph[x][y]=="G":
        visit[x][y]=True
        
        
        dfs_G(x-1,y)
        dfs_G(x,y-1)
        dfs_G(x+1,y)
        dfs_G(x,y+1)
        return True
    return False
def dfs_B(x,y):
    if x>=n or x <=-1 or y<=-1 or y>=n:
        return False

    if visit[x][y]==False and graph[x][y]=="B":
        visit[x][y]=True
        
        
        dfs_B(x-1,y)
        dfs_B(x,y-1)
        dfs_B(x+1,y)
        dfs_B(x,y+1)
        return True
    

    return False

def dfs_RG(x,y):
    if x>=n or x <=-1 or y<=-1 or y>=n:
        return False

    if visit2[x][y]==False and (graph[x][y]=="R" or graph[x][y]=="G"):
        visit2[x][y]=True
        
        
        dfs_RG(x-1,y)
        dfs_RG(x,y-1)
        dfs_RG(x+1,y)
        dfs_RG(x,y+1)
        return True
    

    return False


   
r=0
g=0
b=0
rg=0
house=[]
for i in range(n):
    for j in range(n):
       if visit[i][j]==False:
        if(dfs_R(i,j)==True):
            r+=1
        if(dfs_G(i,j)==True):
            g+=1
        if(dfs_B(i,j)==True):
            b+=1
for i in range(n):
    for j in range(n):
        if visit2[i][j]==False and (graph[i][j]=="R" or graph[i][j]=="G"):
            if(dfs_RG(i,j)==True):
                rg+=1
        

print(r+g+b,rg+b)
