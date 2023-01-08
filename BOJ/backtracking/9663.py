import time
start=time.time()
def promising(i):
    k=1
    flag=True
    while(k<i and flag):
        if(col[i]==col[k] or abs(col[i]-col[k])==(i-k)):
            flag=False
        k+=1
    return flag


def n_queens(i):
    global cnt
    n=len(col)-1
    if promising(i):
        for j in range(1,n+1):
            col

    
            
        
cnt=0
N=int(input()) #n=4
col=[0 for i in range(N+1)]

n_queens(0)
print(cnt)
print("time:",time.time()-start)