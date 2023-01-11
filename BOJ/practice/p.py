import sys
from collections import deque
import heapq
n,l=map(int,input().split())
num=list(map(int,sys.stdin.readline().split())) 
selection=deque()


for i in range(n):
    tmp=num[i]
    

    while selection and selection[-1]>tmp:
        selection.pop()
    selection.append(tmp)
    if i>=l and selection[0]==num[i-l]:
        selection.popleft()
    print(selection[0],end=' ')
