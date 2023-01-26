dist=[0 for i in range(100001)]

N,K=map(int,input().split())

from collections import deque

def find():
    
    q=deque()
    q.append(N)
    while q:
        y=q.popleft()
        if y==K:
            print(dist[y])
            break
        for i in(y*2,y-1,y+1):
            if 0<=i<=100000 and dist[i]==0:
                if i!=y*2:
                    dist[i]=dist[y]+1
                    q.append(i)
        
                else:
                    dist[i]=dist[y]
                    q.append(i)
                
        
        
        

find()


