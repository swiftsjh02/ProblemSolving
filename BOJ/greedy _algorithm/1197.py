from pprint import pprint
import math


v,e=map(int,input().split())
edge=[list(map(int,input().split())) for i in range(e)]
node=[i for i in range(v)]
for i in range(e):
    for j in range(0,2):
        edge[i][j]-=1



print(prim())