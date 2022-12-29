def dijkstra(start):
    distance[start]=0
    visited[start]=True

    for j in graph[start]:
        distance[j[0]]=j[1]

    for i in range(len(graph)-1):
        now=get_smallest_node()
        visited[now]=True
        for j in graph[now]:
            cost=distance[now]+j[1]
            if cost<distance[j[0]]:
                distance[j[0]]=cost
    return distance



def get_smallest_node():
    min_value=float('inf')
    index=0
    for i in range(1,len(graph)):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i

    return index



v,e=map(int,input().split())
k=int(input())
graph=[[] for i in range(v+1)]
distance=[float('inf') for i in range(v+1)]
visited=[False for i in range(v+1)]


for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])

print(graph)

distance=dijkstra(k)
for i in distance:
    print(i)

