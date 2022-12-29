import sys
import heapq

n=int(input())

q1=[]
q2=[]

for i in range(n):
    a=int(sys.stdin.readline())
    if a<0:
        heapq.heappush(q1,-a)
    elif a>0:
        heapq.heappush(q2,a)
    else:
        if not q1:
            if not q2:
                print(0)
            else:
                print(heapq.heappop(q2))
        elif not q2:
            print(-heapq.heappop(q1))
        else:
            tmp1=-heapq.heappop(q1)
            tmp2= heapq.heappop(q2)

            if abs(tmp1)>abs(tmp2):
                print(tmp2)
                heapq.heappush(q1,-tmp1)
            else:
                print(tmp1)
                heapq.heappush(q2,tmp2)