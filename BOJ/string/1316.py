line=int(input())


cnt=0
for i in range(line):
    a=[k for k in input()]
    n=list(0 for j in range(len(a)))
    for i in range(0,len(a)):
        if a[i] in n:
            if n[i-1]!=a[i]:
                cnt+=1
                break
            else:
                n[i]=a[i]
                
        else:
            n[i]=a[i]


print(line-cnt)