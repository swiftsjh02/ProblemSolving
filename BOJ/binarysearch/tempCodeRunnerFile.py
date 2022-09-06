
import sys
sys.setrecursionlimit(100000)

def cut(start,half,target,max_len):
    get=0
    for i in tree:
        if i-half<0:
            pass
        else:
            get+=i-half
 
    if get>=target:
        answer.append(half)
    if get>target:
        start=half
        half=(max_len+start)//2
        cut(start,half,target,max_len)
    if get<target:
        max_len=half
        half=(max_len+start)//2
        cut(start,half,target,max_len)


n,m=map(int,input().split())
tree=list(map(int,input().split()))

max_len=max(tree)
start=0
half=(start+max_len)//2
answer=[]

cut(start,half,m,max_len)

print(max(answer))

