import sys
char=set()
ans=0
def dfs(x,y,count):
    global ans
    ans=max(ans,count)
    
    if 0<=x-1<r and 0<=y<c and not graph[y][x-1] in char:
        
            char.add(graph[y][x-1])
            dfs(x-1,y,count+1)
            char.remove(graph[y][x-1])
    if 0<=x+1<r and 0<=y<c and not graph[y][x+1] in char:
        
            char.add(graph[y][x+1])
            dfs(x+1,y,count+1)
            char.remove(graph[y][x+1])
    if 0<=x<r and 0<=y-1<c and not graph[y-1][x] in char:
        
            char.add(graph[y-1][x])
            dfs(x,y-1,count+1)
            char.remove(graph[y-1][x])
    if 0<=x<r and 0<=y+1<c and not graph[y+1][x] in char:
        
            char.add(graph[y+1][x])
            dfs(x,y+1,count+1)
            char.remove(graph[y+1][x])
    
    

graph=[]
r,c=map(int,sys.stdin.readline().split())
visit=[[0 for i in range(c)] for i in range(r)]
for i in range(r):
    graph.append(list(sys.stdin.readline()))

char.add(graph[0][0])
dfs(0,0,1)
print(ans)