import heapq
import sys
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance=[float('inf') for i in range(v+1)]
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance



v,e,x=map(int,input().split())
graph=[[] for i in range(v+1)]




for i in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append([b,c])


max_value=0
for i in range(1,v+1):
    d1=dijkstra(i)
    d2=dijkstra(x)
    if max_value<d1[x]+d2[i]:
        max_value=d1[x]+d2[i]
print(max_value)
    




