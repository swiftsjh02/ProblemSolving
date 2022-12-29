from pprint import pprint



def dijkstra(graph,start):
    #initialize distance
    distance=[float('inf') for i in range(0,len(graph))]
    distance[start]=0
    visited=[False for i in range(len(graph))]
    visited[start]=True

    for i in graph[start]:
        if i!=0:
            distance[graph[start].index(i)]=i
    
    for i in range(len(graph)-1):
        u=get_min_distance(distance,visited)
        visited[u]=True
        for v in range(len(graph)):
            if graph[u][v]!=0 and visited[v]==False:
                distance[v]=min(distance[v],distance[u]+graph[u][v])
    
    return distance

def get_min_distance(distance, visited):
    min_distance=float('inf')
    min_index=-1
    for i in range(len(distance)):
        if distance[i]<min_distance and visited[i]==False:
            min_distance=distance[i]
            min_index=i
    return min_index     



n,m,k,x=map(int,input().split())

graph=[[0 for i in range(n)] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1

pprint(graph)    

distance=dijkstra(graph,x-1)


print(distance)
answer=[]
for i in range(len(distance)):
    if distance[i]==k:
        answer.append(i)

if len(answer)==0:
    print(-1)
else:
    for e in answer:
        print(e)
    

