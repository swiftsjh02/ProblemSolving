
import sys
from collections import deque
q=deque([])

n=int(sys.stdin.readline())



for i in range(n):
    a=[k for k in sys.stdin.readline().split()]
    
    if a[0]=="push":
        q.append(int(a[1]))
    if a[0]=="pop":
        try:
            print(q.popleft())
        except:
            print("-1")
    if a[0]=="front":
        if len(q)==0:
            print("-1")
        else:
            print(q[0])
    if a[0]=="back":
        if len(q)==0:
            print("-1")
        else:
            print(q[len(q)-1])
    if a[0]=="empty":
        if len(q)==0:
            print("1")
        else:
            print("0")
    if a[0]=="size":
        print(len(q))
        

    

