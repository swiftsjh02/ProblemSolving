n,m = map(int,input().split()) # n x m 배열 입력 

graph=[]
for i in range(n): 
    graph.append(list(map(int,input())))

def dfs(x,y): ## Searching continuously connected node which was not visited (node that has 1 as value) once done return True
    if x<= -1 or x>=n or y<= -1 or y>=m: #when x ,y reach out of bound then return false
        return False
    
    if graph[x][y]==0: #when met node not visited 
        graph[x][y]=1 # check node as visited

        # recursively check nearby node
        dfs(x-1,y) 
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True # when all node was checked then Return True

    return False


result=0 
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1

print(result)