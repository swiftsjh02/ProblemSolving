

def dijkstra(graph,start):
    #initialize distance
    distance=[float('inf') for i in range(len(graph))]
    distance[start]=0
    #initialize visited
    visited=[False for i in range(len(graph))]
    #initialize queue
    queue=[i for i in range(len(graph))]
    #loop until queue is empty
    while queue:
        #find minimum distance node
        min_node=queue[0]
        for i in queue:
            if distance[i]<distance[min_node]:
                min_node=i
        #remove min_node from queue
        queue.remove(min_node)
        #update distance
        for i in range(len(graph)):
            if graph[min_node][i]!=0 and visited[i]==False:
                if distance[min_node]+graph[min_node][i]<distance[i]:
                    distance[i]=distance[min_node]+graph[min_node][i]
                    
        #update visited
        visited[min_node]=True
    return distance


#input graph
graph=[[0,4,0,0,0,0,0,8,0],
         [4,0,8,0,0,0,0,11,0],
            [0,8,0,7,0,4,0,0,2],
            [0,0,7,0,9,14,0,0,0],
            [0,0,0,9,0,10,0,0,0],
            [0,0,4,14,10,0,2,0,0],
            [0,0,0,0,0,2,0,1,6],
            [8,11,0,0,0,0,1,0,7],
            [0,0,2,0,0,0,6,7,0]]

#input start node
start=0

#call dijkstra algorithm
distance=dijkstra(graph,start)

#print distance
print("Distance from node "+str(start)+" to other nodes:")
for i in range(len(distance)):
    print("Node "+str(i)+": "+str(distance[i]))
    
