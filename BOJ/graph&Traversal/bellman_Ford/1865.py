from collections import deque
from pprint import pprint
def bellman_ford():
    distance=[10001 for i in range(n+1)]
    for i in range(n):
        for a,b,c in edge:
            if distance[b]>distance[a]+c:
                if i==n-1:
                    return -1
                distance[b]=distance[a]+c
    return distance
   


                
for t in range(int(input())):  
    n,m,w=map(int,input().split())
    edge=[]
    for i in range(m):
        a,b,c=map(int,input().split())
        edge.append((a,b,c))
        edge.append((b,a,c))
    for i in range(w):
        a,b,c=map(int,input().split())
        edge.append((a,b,-c))

    dist=bellman_ford()
    if dist==-1:
        print("YES")
    else:
        print("NO")