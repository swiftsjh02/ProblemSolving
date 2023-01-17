# Union by Rank를 이용해서 트리 구조가 링크드리스트처럼 한쪽으로 길어져서
#시간 복잡도가 O(N)에 가까워 지는것을 막음

import sys
sys.setrecursionlimit(10**5)
def getParent(x): ## x의 부모 찾기
    if(parent[x]!=x):
        parent[x]=getParent(parent[x])
    return parent[x]

def unionParent(b,c): # a와 b의 부모를 합침
    b=getParent(b)
    c=getParent(c)
    if(b==c):
        return
    if(node_rank[b]<node_rank[c]):#b의 높이가 더 낮으면
        parent[b]=c
    else: # c의 높이가 크거나 같으면
        parent[c]=b
        
    
    if(node_rank[b]==node_rank[c]):
        node_rank[b]=node_rank[b]+1




n,m=map(int,input().split())
parent=[0 for i in range(n+1)]
node_rank=[0 for i in range(n+1)]
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





