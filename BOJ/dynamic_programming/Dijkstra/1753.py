import heapq
import sys
def dijkstra(graph,start):
    q=[]
    distance=[float('inf') for i in range(0,len(graph))]
    visited=[False for i in range(len(graph))]
    distance[start]=0
    heapq.heappush(q,[0,start])
    while q:
        dist,now=heapq.heappop(q)
        if visited[now]==False:
            visited[now]=True
            for i in graph[now]:
                cost=dist+i[1]
                if cost<distance[i[0]]:
                    distance[i[0]]=cost
                    heapq.heappush(q,[cost,i[0]])
    return distance
    
    



v,e=map(int,sys.stdin.readline().split())
k=int(sys.stdin.readline())

graph=[[] for i in range(v)]
for i in range(e):
    u,v,w=map(int,sys.stdin.readline().split())
    graph[u-1].append([v-1,w])


distance=dijkstra(graph,k-1)
for i in distance:
    if i==float('inf'):
        print('INF')
    else:
        print(i)



