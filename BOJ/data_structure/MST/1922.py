import sys
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

v=int(input())
e=int(input())
edge=[]
parent=[0 for i in range(v)]
for i in range(v):
    parent[i]=i
for i in range(e):
    a,b,d=map(int,sys.stdin.readline().split())
    edge.append([a-1,b-1,d])

edge.sort(key=lambda x:x[2])

sum=0

for i in range(e):
    if(findParent(edge[i][0],edge[i][1])==0):
        sum=sum+edge[i][2]
        unionParent(edge[i][0],edge[i][1])
    
print(sum)
