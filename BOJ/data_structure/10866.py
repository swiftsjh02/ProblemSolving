
import sys
from collections import deque
dq=deque([])

n=int(sys.stdin.readline())



for i in range(n):
    a=[k for k in sys.stdin.readline().split()]
    
    if a[0]=="push_front":
        dq.appendleft(int(a[1]))
    if a[0]=="push_back":
        dq.append(int(a[1]))
    if a[0]=="pop_front":
        try:
            print(dq.popleft())
        except:
            print("-1")
    if a[0]=="pop_back":
        try:
            print(dq.pop())
        except:
            print("-1")
    if a[0]=="front":
        if len(dq)==0:
            print("-1")
        else:
            print(dq[0])
    if a[0]=="back":
        if len(dq)==0:
            print("-1")
        else:
            print(dq[len(dq)-1])
    if a[0]=="empty":
        if len(dq)==0:
            print("1")
        else:
            print("0")
    if a[0]=="size":
        print(len(dq))
        

    

