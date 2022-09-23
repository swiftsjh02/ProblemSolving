from pprint import pprint
from bisect import bisect_left

i=0
elephant=[]
while True:
    try:
        tmp=list(map(int,input().split()))
        tmp.append(i+1)
        elephant.append(tmp)
        i+=1
    except EOFError:
        break

elephant.sort(key=lambda x:x[0],reverse=True)


dp=[]
for i in range(0,len(elephant)):
    pos=bisect_left(dp,elephant[i][1])
    if len(dp)<=pos:
        dp.append(elephant[i][1])
    else:
        dp[pos]=elephant[i][1]



answer=[]
for e in dp:
    for i in range(len(elephant)):
        if elephant[i][1]==e:
            answer.append(elephant[i][2])

print(len(answer))

for e in answer:
    print(e)
            
    