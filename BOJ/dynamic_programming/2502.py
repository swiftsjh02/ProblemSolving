from pprint import pprint
d,k=map(int,input().split())
target=[0 for i in range(d)]
target[0]='a'
target[1]='b'
for i in range(2,len(target)):
    target[i]=target[i-1]+target[i-2]


max_a=0
max_b=0
for i in target:
    temp_a=0
    temp_b=0
    for j in i:
        if j=='a':
            temp_a+=1
        elif j=='b':
            temp_b+=1
    if temp_a>max_a:
        max_a=temp_a
    if temp_b>max_b:
        max_b=temp_b


        
division=(k//max(max_a,max_b))+1

table=[[0 for i in range(division+1)] for j in range(2)]

cnt=0
for i in range(1,division+1):
    
    for j in range(1,division+1):
        if i<=j:
            table[i-cnt][j]=i*max_a+j*max_b
            if table[i-cnt][j]==k:
                print(i)
                print(j)
                quit()
    cnt+=1




