

N,K=map(int,input().split())
visit=set()
from collections import deque

def find():
    
    q=deque([(N,0)])
    while q:
        y,t=q.popleft()
        if y==K:
            print(t)
            break
        for i in(y*2,y+1,y-1):
            if 0<=i<=100000 and i not in visit:
                q.append((i,t+1))
                visit.add(i)
        
             

find()
