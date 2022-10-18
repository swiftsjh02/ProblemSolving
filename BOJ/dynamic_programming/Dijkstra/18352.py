from pprint import pprint


def dijkstra(graph,start):
    #initialize distance
    distance=[-1 for i in range(0,len(graph))]
    distance[start]=0
    #initialize queue
    queue=[start]

    #print(distance)
    #print(visited)
    #print(queue)

    while len(queue)!=0:
        v=queue.pop(0)
        for i in range(0,len(distance)):
            if distance[i]==-1 and graph[v][i]==1:
                distance[i]=min(distance[i],distance[i]+1)
                
        
    return distance





n,m,k,x=map(int,input().split())

graph=[[0 for i in range(n)] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1

pprint(graph)    

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
    

