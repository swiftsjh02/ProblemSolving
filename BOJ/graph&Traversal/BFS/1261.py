from collections import deque
import sys
sys.setrecursionlimit(10**9)
graph=[]
n,m=map(int,input().split())
for i in range(m):
    graph.append(list(input()))
cnt=[]
print(graph)
temp=0
def dfs(y,x):
    global temp
    if y<0 or y>=n or x<0 or x>=m:
        return
    if y==n-1 and x==m-1:
        print("found")
        cnt.append(temp)
        return
    if graph[y][x]==1:
        temp+=1
    
    dfs(y-1,x)
    dfs(y+1,x)
    dfs(y,x+1)
    dfs(y,x-1)
    temp-=1
    return
    
    
    

dfs(0,0)
