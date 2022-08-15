
import sys
a=[0]*10001

for i in range(int(sys.stdin.readline())):
    t=int(sys.stdin.readline())
    a[t-1]+=1


for i in range(10001):
    if a[i]!=0:
        for j in range(a[i]):
            print(i+1)
