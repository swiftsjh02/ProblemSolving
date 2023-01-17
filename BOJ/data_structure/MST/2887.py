import sys

def union(x,y):
    x = find(x)
    y = find(y)
    parents[y] = x

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

n = int(input())
xlst,ylst,zlst = [],[],[]
for i in range(n):
    x,y,z = map(int,input().split())
    xlst.append((x,i))
    ylst.append((y,i))
    zlst.append((z,i))
xlst.sort()
ylst.sort()
zlst.sort()





edges = []
for curList in xlst,ylst,zlst:
    print(curList)
    for i in range(1,n):
        w1,a = curList[i-1]
        w2,b = curList[i]
        edges.append((abs(w1-w2),a,b))
edges.sort(reverse = True)

print(edges)

parents = [i for i in range(n+1)]
cnt,ans = n-1,0
while cnt:
    w,a,b = edges.pop()
    if find(a) == find(b):
        continue
    union(a,b)
    cnt-=1
    ans+=w
print(ans)