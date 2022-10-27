from pprint import pprint
n,m=map(int,input().split())
graph=[[0 for i in range(n)] for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a-1][b-1]=c


def bellmanford(start):
    global n,m
    dist=[float('inf') for i in range(len(graph))]
    dist[start]=0
    


    