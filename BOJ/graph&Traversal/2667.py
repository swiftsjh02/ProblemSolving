



n=int(input())
graph=[]
visit=[[False for i in range(n)] for k in range(n)]

for i in range(n):
    graph.append(list(map(int,input())))


def dfs(x,y):
    if x>=n or x <=-1 or y<=-1 or y>=n:
        return False
    global cnt
    if visit[x][y]==False and graph[x][y]==1:
        visit[x][y]=True
        cnt+=1
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

cnt=0    
result=0
house=[]
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result+=1
            house.append(cnt)
            cnt=0

print(result)
house.sort()
for l in house:
    print(l)