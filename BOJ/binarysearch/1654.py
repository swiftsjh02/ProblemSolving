import sys


k,n=map(int,input().split())
lan=[]
for i in range(k):
    lan.append(int(input()))


max_lan=max(lan)
start=1
half=(max_lan+start)//2
answer=[]


while start<=max_lan:
    count=0
    for i in lan:
        count+=i//half
    if count>=n:
        answer.append(half)
        start=half+1
    else:
        max_lan=half-1
    half=(start+max_lan)//2

print(max(answer))

