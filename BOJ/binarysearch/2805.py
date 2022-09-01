
import sys
sys.setrecursionlimit(100000)

def cut(half,target,max_len):
    get=0
    for i in tree:
        if i-half<0:
            get+=0
        else:
            get+=i-half
 
    if get==target:
        print(half)
    if get>target:
        cut(max_len-(half//2),target,max_len)
    if get<target:
        cut(half//2,target,max_len)


#n,m=map(int,input().split())
#tree=list(map(int,input().split()))
n=5
m=20
tree=[4,42,40,26,46]
max_len=max(tree)
half=max_len//2

(cut(half,m,max_len))

