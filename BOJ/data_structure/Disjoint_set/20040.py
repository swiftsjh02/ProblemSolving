import sys
sys.setrecursionlimit(10**4)
def getParent(x): ## x의 부모 찾기
    if(parent[x]!=x):
        parent[x]=getParent(parent[x])
    return parent[x]

def unionParent(b,c): # a와 b의 부모를 합침
    b=getParent(b)
    c=getParent(c)
    if(b<c):
        parent[c]=b
    else:
        parent[b]=c



t=[]
n,m=map(int,input().split())
parent=[0 for i in range(n+1)]
for i in range(n+1):
    parent[i]=i
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    
    if(getParent(a+1)==getParent(b+1)):
        t.append(i+1)
    else:
        unionParent(a+1,b+1)

if len(t)==0:
    print(0)
else:
    print(t[0])
