import math

def isPrime(x):

    if x==1:
        return False

    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

input()
cnt=0
nums=[int(k) for k in input().split()]

for i in nums:
    if isPrime(i)==True:
        cnt+=1

print(cnt)

