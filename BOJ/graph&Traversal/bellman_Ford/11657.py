from collections import deque
from pprint import pprint
def bellman_ford():
    distance=[float('inf') for i in range(n+1)]
    distance[1]=0
    for i in range(n):
        for a,b,c in edge:
            if distance[a]!=float('inf') and distance[b]>distance[a]+c:
                if i==n-1:
                    return -1
                distance[b]=distance[a]+c
    return distance
   


                
    
n,m=map(int,input().split())
edge=[]
for i in range(m):
    a,b,c=map(int,input().split())
    edge.append((a,b,c))

dist=bellman_ford()
if dist!=-1:
    for i in range(2,n+1):
        if dist[i]==float('inf'):
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)
