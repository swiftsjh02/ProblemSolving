import sys


def dfs(r): 
    visited[r]=True
    print(r,end=" ")
    for e in node[r]:
        if visited[e]==False:
            dfs(e)
    

n,m,r=map(int,input().split())



visited=[False]*(n+1)
node=[[]*n for k in range(n+1)]


for z in range(m):
    com=list(map(int,sys.stdin.readline().split()))
    node[com[0]].append(com[1])
    node[com[1]].append(com[0])
    


    
dfs(r)
print()




