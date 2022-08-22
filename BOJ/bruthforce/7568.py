from pprint import pprint

a=[]

for i in range(int(input())):
    tmp=[int(k) for k in input().split()]
    a.append(tmp)

cnt=[]

for i in range(len(a)):
    tmp=0
    for j in range(len(a)):
        if a[i][0]<a[j][0]:
            if a[i][1]<a[j][1]:
                tmp+=1
    cnt.append(tmp+1)

for i in cnt:
    print(i,end=" ")
