import sys
sys.setrecursionlimit(1000000)
from pprint import pprint

n=int(input())

def dfs(y,x,k):
    if y<=-1 or y>=n or x<=-1 or x>=n:
        return False
    if visit[y][x]==True:
        return False
    else:
        visit[y][x]=True

    if a[y][x]<=k:
        return False
  

    dfs(y,x-1,k)
    dfs(y,x+1,k)
    dfs(y-1,x,k)
    dfs(y+1,x,k)
    return True



ans=0
max=0
a=[]
visit=[[False for i in range(n)] for i in range(n)] 
for i in range(n):
    tmp=list(map(int,input().split()))
    for i in tmp:
        if i>max:
            max=i
    a.append(tmp)

        

    
result=0
    
for k in range(0,max+1):
    result=0
    visit=[[False for i in range(n)] for i in range(n)] 
    for i in range(n):
        for j in range(n):
            if dfs(i,j,k)==True:
                result+=1
    if ans<result:
        ans=result

print(ans)

   
