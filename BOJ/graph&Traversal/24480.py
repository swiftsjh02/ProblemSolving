import sys
sys.setrecursionlimit(100000)

def dfs(r): 
    global cnt
    visited[r]=True
    answer[r]=cnt
    cnt+=1
   
    for e in node[r]:
        if visited[e]==False:
            dfs(e)
            
    

n,m,r=map(int,input().split())


cnt=1
answer=[0]*(n+1)
visited=[False]*(n+1)
node=[[]*n for k in range(n+1)]


for z in range(m):
    com=list(map(int,sys.stdin.readline().split()))
    node[com[0]].append(com[1])
    node[com[1]].append(com[0])
    
  
for i in range(len(node)):
    node[i].sort(reverse=True)



dfs(r)

for i in range(1,n+1):
    print(answer[i])

