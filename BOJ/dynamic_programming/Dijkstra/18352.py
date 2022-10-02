from pprint import pprint


def dijkstra(graph,start):
    #initialize distance
    distance=[float('inf') for i in range(0,len(graph))]
    distance[start]=0
    #initialize visited
    visited=[False for i in range(0,len(graph))]
    #initialize queue
    queue=[i for i in range(0,len(graph))]

    #print(distance)
    #print(visited)
    #print(queue)

    while len(queue)!=1:
        min=queue[0]
        for i in queue[1:]:
            if distance[i]<distance[min]:
                min=i
        queue.remove(min)

        for i in range(len(graph)):
            if graph[min][i]!=0 and visited[i]==False:
                if distance[min]+graph[min][i]<distance[i]:
                    distance[i]=distance[min]+graph[min][i]
                    
        #update visited
        visited[min]=True
    return distance





n,m,k,x=map(int,input().split())

graph=[[0 for i in range(n+1)] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

#pprint(graph)    

distance=dijkstra(graph,x)
answer=[]
for i in range(len(distance)):
    if distance[i]==k:
        answer.append(i)

if len(answer)==0:
    print(-1)
else:
    for e in answer:
        print(e)
    

