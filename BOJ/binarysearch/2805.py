
import sys
sys.setrecursionlimit(1000000)

def cut(start,half,target,max_len):
    if half==max_len or half==start:
        if len(answer)==0:
            print("0")
            exit()
            
        print(min(answer,key=answer.get))
        exit()


    get=0
    for i in tree:
        if i-half<0:
            pass
        else:
            get+=i-half
    if get==target:
        print(half)
        exit()
    if get>target:
        answer[half]=get
        start=half
        half=(max_len+start)//2
        cut(start,half,target,max_len)
    if get<target:
        max_len=half
        half=(max_len+start)//2
        cut(start,half,target,max_len)


n,m=map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))

max_len=max(tree)
start=0
half=(start+max_len)//2
answer={}

cut(start,half,m,max_len)



