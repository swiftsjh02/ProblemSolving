lis=list(map(int,input().split()))
dpfull=list()

pos=0

while pos<=len(lis)-1:
    dp=[]
    for i in lis[pos:]:
        if len(dp)==0:
            dp.append(i)
        else:
            if dp[-1]<i and dp[-2]<i:
                dp.append(i)
            else:
                dp[-1]=i
    dpfull.append(dp)
    pos+=1


print(dp)
            