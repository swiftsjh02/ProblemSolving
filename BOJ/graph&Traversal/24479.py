import sys


def dfs(r): 
    global cnt
    visited[r]=True
   
    for e in node[r]:
        if visited[e]==False:
            dfs(e)
            cnt+=1
    

n=int(input())
m=int(input())

cnt=0
visited=[False]*(n+1)
node=[[]*n for k in range(n+1)]


for z in range(m):
    com=list(map(int,sys.stdin.readline().split()))
    node[com[0]].append(com[1])
    node[com[1]].append(com[0])
    


    
dfs(1)
print(cnt)



