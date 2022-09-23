from pprint import pprint
from bisect import bisect_left

input()
A=list(map(int,input().split()))


dp=[1 for i in range(len(A))]

for i in range(len(A)):
    for j in range(i):
        if A[i]>A[j]:
            dp[i]=max(dp[i],dp[j]+1)


max_dp=max(dp)


max_idx=dp.index(max_dp)
lis=[]

while max_idx>=0:
    if dp[max_idx]==max_dp:
        lis.append(A[max_idx])
        max_dp-=1
    max_idx-=1


lis.reverse()
print(len(lis))
for i in lis:
    print(i,end=" ")