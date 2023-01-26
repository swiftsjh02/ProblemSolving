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





v,e=map(int,input().split())
graph=[[] for i in range(v+1)]




for i in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


k,d=map(int,input().split())
d1=dijkstra(1)
d2=dijkstra(k)
d3=dijkstra(d)


result=min(d1[k]+d2[d]+d3[v],d1[d]+d3[k]+d2[v])
if result==float('inf'):
    print(-1)
else: print(result)


