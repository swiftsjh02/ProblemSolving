import sys
def getParent(x): ## x의 부모 찾기
    if(parent[x]==x):
        return x
    parent[x]=getParent(parent[x])
    return parent[x]

def unionParent(a,b): # a와 b의 부모를 합침
    a=getParent(a)
    b=getParent(b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b

def findParent(a,b): #부모를 찾고 둘이 부모가 같으면 1 다르면 0 리턴
    a=getParent(a)
    b=getParent(b)
    if(a==b):
        return 1
    else:
        return 0

parent=[0]#원소의 개수만큼 0으로 초기화 