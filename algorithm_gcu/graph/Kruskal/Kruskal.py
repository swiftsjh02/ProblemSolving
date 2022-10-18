v,e= map(int, input().split())
edges=[]
id=[{i} for i in range(v)]
for i in range(e):
    s,d,w= map(int, input().split())
    edges.append([s-1,d-1,w])

edges.sort(key=lambda x:x[2])

def check(s,d):
    if d not in id[s]:
        id[s]=id[s].union(id[d])
        id.pop(d)
        return False
    return True



print(edges)
print(id)

answer=0

for e in edges:
    if check(e[0],e[1])==False:
        answer+=e[2]
    else:
        continue
    

print(answer)
