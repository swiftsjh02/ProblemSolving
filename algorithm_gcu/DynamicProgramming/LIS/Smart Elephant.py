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
    except:
        break

elephant.sort(key=lambda x:x[0],reverse=True)


dp=[1 for i in range(len(elephant))]

for i in range(len(elephant)):
    for j in range(i):
        if elephant[i][1]>elephant[j][1]:
            dp[i]=max(dp[i],dp[j]+1)


max_dp=max(dp)



max_idx=dp.index(max_dp)
lis=[]

while max_idx>=0:
    if dp[max_idx]==max_dp:
        lis.append(elephant[max_idx][2])
        max_dp-=1
    max_idx-=1



print(len(lis))
for i in lis:
    print(i)