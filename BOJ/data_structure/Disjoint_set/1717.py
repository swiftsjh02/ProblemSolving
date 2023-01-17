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




n,m=map(int,input().split())
parent=[0 for i in range(n+1)]
for i in range(n+1):
    parent[i]=i
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if a==0:
        unionParent(b,c)
    else:
        if(getParent(b)==getParent(c)):
            print("YES")
        else:
            print("NO")





