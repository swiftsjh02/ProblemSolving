import sys

def cut(start,half,target,max_len):

    if target==1:
        print(max(lan))
        exit()

    if half==max_len or half==start:

        if len(answer)==0:
            print(max(lan))
            exit()
        
        print(max(answer))
        exit()

    get=0
    for i in lan:
        if i//half>0:
            get+=i//half
    

    
    if get==target:
        print(half)
        exit()
    if get>target:
        answer.append(half)
        start=half
        half=(max_len+start)//2
        cut(start,half,target,max_len)
    if get<target:
        max_len=half
        half=(max_len+start)//2
        cut(start,half,target,max_len)


k,n=map(int,input().split())
lan=[]
for i in range(k):
    lan.append(int(input()))


max_lan=max(lan)
half=max_lan//2
start=0
answer=[]


cut(start,half,n,max_lan)   

