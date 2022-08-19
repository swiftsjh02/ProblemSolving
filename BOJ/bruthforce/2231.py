n=int(input())
m=[]
for i in range(1,n):
    i=str(i)
    sum=int(i)
    for k in i:
        sum=sum+int(k)
    if(sum==n):
        m.append(int(i))


if len(m)==0:
    print(0)
    quit()



print(min(m))