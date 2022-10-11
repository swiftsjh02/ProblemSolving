import math
from pprint import pprint
def distance(node1,node2):
    return math.sqrt((node1[0]-node2[0])**2+(node1[1]-node2[1])**2)



def prim():
    n=len(node)
    start=0
    visited=set()
    visited.add(start)
    distance=0

    for i in range(n-1):
        min_dist,next_node = math.inf, -1

        for v in visited:
            for j in range(0,n):
                if j not in visited and 0<matrix[v][j]<min_dist:
                    min_dist=matrix[v][j]
                    next_node=j
        distance+=min_dist
        visited.add(next_node)
    
    return distance

        


n=int(input())
input=[list(map(float,input().split())) for i in range(n)]
node=[0 for i in range(n)]
matrix=[[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if(matrix[i][j]==0):
            matrix[i][j]=distance(input[i],input[j])
        else:
            pass



print(round(prim(),2))