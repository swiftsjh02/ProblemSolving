import sys


def dfs(node,r):
    
    answer.append(r)
    
    visited[r]=True
   
    for e in node[r]:
        if visited[e]==False:
            dfs(node,e)
    

n=int(input())
m=int(input())

answer=[]
visited=[False]*(n+1)
node=[]
for j in range(n+1):
        node.append([])

for i in range(m):
    com=list(map(int,sys.stdin.readline().split()))
    node[com[0]].append(com[1])
    node[com[1]].append(com[1])
    node[com[0]].sort()


    
dfs(node,1)



print(len(answer)-1)

