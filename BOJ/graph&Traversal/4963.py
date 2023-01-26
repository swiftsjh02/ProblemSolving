from collections import deque

def dfs(y,x,width,height):
    if y<=-1 or y>=height or x<=-1 or x>=width:
        return False

    if graph[y][x]==1:
        graph[y][x]=0

        dfs(y,x-1,width,height)
        dfs(y,x+1,width,height)
        dfs(y-1,x,width,height)
        dfs(y+1,x,width,height)
        dfs(y-1,x-1,width,height)
        dfs(y+1,x-1,width,height)
        dfs(y-1,x+1,width,height)
        dfs(y+1,x+1,width,height)
        return True
    return False


while True:
    w,h=map(int,input().split())
    cnt=0
    if w ==0 and h==0:
        break
    graph=[]
    for i in range(h):
        graph.append(list(map(int,input().split())))
    
    for i in range(h):
        for j in range(w):
            if dfs(i,j,w,h)==True:
                cnt+=1
    print(cnt)


