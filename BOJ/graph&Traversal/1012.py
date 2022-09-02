import sys
sys.setrecursionlimit(1000000)
from pprint import pprint

def dfs(y,x):
    if y<=-1 or y>=n or x<=-1 or x>=m:
        return False

    if a[y][x]==1:
        a[y][x]=0

        dfs(y,x-1)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y+1,x)
        return True
    return False


for i in range(int(input())):
    m,n,k=map(int,input().split())
    a=[[0]*m for k in range(n)]
    
    for i in range(k):
        x,y=map(int,input().split())
        a[y][x]=1
        

    

    result=0

    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1

    print(result)
