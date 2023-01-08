import heapq
import sys
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
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





v=int(sys.stdin.readline())
e=int(sys.stdin.readline())
graph=[[] for i in range(v+1)]
distance=[float('inf') for i in range(v+1)]



for i in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append([b,c])


k,d=map(int,input().split())
dijkstra(k)
print(distance[d])

