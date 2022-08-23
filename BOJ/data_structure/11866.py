from collections import deque

k=[int(k) for k in input().split()]

q=deque([])
deleted=[]

for i in range(1,k[0]+1):
    q.append(i)

c=1
while len(q)!=0:
    if c!=k[1]:
        tmp=q.popleft()
        q.append(tmp)
        c+=1
    elif c==k[1]:
        deleted.append(str(q.popleft()))
        c=1

print("<%s>" %(", ".join(deleted)))

        

        

