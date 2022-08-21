from heapq import heappop,heappush
import sys


heaps=[]
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    if n!=0:
        heappush(heaps,-n)
    elif len(heaps)!=0:
        print(-heappop(heaps))
    else:
        print(0)