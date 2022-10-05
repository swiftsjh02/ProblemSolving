import pprint

count=0

def graphsolve(graph,queue,visited):
    global count
    while True:
        node=queue[0]
        queue.remove(node)
        visited[node]=True
        for i in range(len(graph[0])):
            if graph[node][i]==1 and visited[i]==False:
                queue.remove(i)
                visited[i]=True
        if len(queue)!=0:
            count+=1
        elif len(queue)==0:
            break
       
    

n,m=map(int,input().split())
graph=[[0 for i in range(n)] for _ in range(n)]
queue=[i for i in range(0,n)]
visited=[False for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

pprint.pprint(graph)

graphsolve(graph,queue,visited)

print(count)



