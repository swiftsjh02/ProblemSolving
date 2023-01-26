char=set()
def dfs(x,y):

    if x>=c or x <=-1 or y<=-1 or y>=r:
        return False

    if visit[y][x]==False:
        visit[y][x]=True
        if char.isdisjoint(graph[y][x])==True:
            char.add(graph[y][x])
            print(graph[y][x])
        else:
            return
    else:
        return

    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
    
    
    


graph=[]
r,c=map(int,input().split())
visit=[[0 for i in range(c)] for i in range(r)]
for i in range(r):
    tmp=input()
    s=[]
    for j in tmp:
        s.append(j)
    graph.append(s)


dfs(0,0)

print(len(char))
    