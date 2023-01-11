n,x=map(int,input().split())
visit=list(map(int,input().split()))
result=[]
max=0
for i in range(x):
    max+=visit[i]
result.append(max)


cnt=0 
tmp=max
for i in range(1,n-x+1):
    tmp=tmp-visit[i-1]
    tmp=tmp+visit[i+x-1]
 
    result.append(tmp)
    if tmp>max:
        max=tmp



if(max==0):
    print("SAD")
else:
    print(max)
    for i in result:
        if i==max:
            cnt+=1
    print(cnt)

        