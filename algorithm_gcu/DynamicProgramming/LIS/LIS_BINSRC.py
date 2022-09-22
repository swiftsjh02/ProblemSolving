from bisect import bisect_left


input()
A=list(map(int,input().split()))
dp=[]

for e in A:
    pos=bisect_left(dp,e) #find the  proper position of e in dp
    print(pos)
    if len(dp)<=pos: # if position of current element is last of dp(current element is biggest element in dp)
        dp.append(e) #then append current element to last position of dp
    else:
        dp[pos]=e

print(len(dp))