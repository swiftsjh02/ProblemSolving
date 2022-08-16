import math
import sys
ans=list()
avg=0
max=-4001
min=4001
max_f=0

n=int(sys.stdin.readline())
nums={}
freq=[]
for k in range(n):
    tmp=int(sys.stdin.readline())
    if tmp in nums.keys():
        nums[tmp]+=1
    else:
        nums[tmp]=1
    if tmp>max:
        max=tmp
    if min>tmp:
        min=tmp
    ans.append(tmp)
    avg=avg+tmp

for a,b in nums.items():
    if max_f<b:
        max_f=b
for a,b in nums.items():
    if b==max_f:
        freq.append(a)



ans.sort()
freq.sort()
print(round(avg/len(ans)))
print(ans[int(len(ans)/2)])
try:
    print(freq[1])
except:
    print(freq[0])
print(max-min)



