a,b=map(int,input().split())
count=0
while a!=b:
    if b<a:
        print(-1)
        exit()
    if b%2==0:
        b=b//2
        count+=1
    elif b%2!=0 and str(b)[-1]=="1":
        b=str(b)
        b=b[0:-1]
        b=int(b)
        count+=1
    else:
        print(-1)
        exit()

print(count+1)

