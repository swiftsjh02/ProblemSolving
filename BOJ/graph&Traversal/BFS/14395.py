from collections import deque
move=["*","+","-","//"]
record=[]
visit=set()
def bfs(start,target):
    if start==target:
        print("0")
        return
    q=deque()
    q.append((start,''))
    while q:
        node,oper=q.popleft()
        
        if node==target:
            print(oper)
            return 0
        
        for i in move:
            nx=0
            if i=="//":
                nx=1
                if 0<=nx<=10e9 and nx not in visit:
                    q.append((nx,oper+"/"))
                    visit.add(nx)
            else:
                nx=eval(str(node)+i+str(node))
                if 0<=nx<=10e9 and nx not in visit:
                    q.append((nx,oper+i))
                    visit.add(nx)
                    
    return -1
    

            
        

    
s,t=map(int,input().split())
if bfs(s,t)==-1:
    print(-1)