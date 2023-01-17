import sys
import math
def getParent(x):
    if(parent[x]==x):
        return x
    parent[x]=getParent(parent[x])
    return parent[x]

def unionParent(a,b):
    a=getParent(a)
    b=getParent(b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b

def findParent(a,b):
    a=getParent(a)
    b=getParent(b)
    if(a==b):
        return 1
    else:
        return 0

def dist(a,b):
    t=node[a]
    c=node[b]

    return math.sqrt(abs(c[0]-t[0])**2+abs(c[1]-t[1])**2)
    



v,m=map(int,input().split())
edge=[]
node=[]
con=[[-1 for i in range(v)] for i in range(v)]


parent=[0 for i in range(v+1)]
for i in range(v):
    parent[i]=i
for i in range(v):
    a,b=map(float,sys.stdin.readline().split())
    node.append([a,b])
for i in range(v-1):
    for j in range(0,v):
        if i!=j and j>i:
            con[i][j]=1

for i in range(v):
    for j in range(v):
        if(con[i][j]==1):
            edge.append([i,j,dist(i,j)])

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    unionParent(a-1,b-1)
    edge.append([a-1,b-1,dist(a-1,b-1)])


edge.sort(key=lambda x:x[2])


sum=0
for i in range(len(edge)):
    if(findParent(edge[i][0],edge[i][1])==0):
        sum+=edge[i][2]
        unionParent(edge[i][0],edge[i][1])


print("{:.2f}".format(sum))