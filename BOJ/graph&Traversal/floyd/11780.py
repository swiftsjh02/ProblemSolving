from pprint import pprint
def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j]=min(graph[i][k]+graph[k][j],graph[i][j])


n=int(input())
m=int(input())
graph=[[float('inf') for i in range(n)] for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a-1][b-1]=c
for i in range(n):
    for j in range(n):
        if i==j:
            graph[i][j]=0
floyd()

pprint(graph)

