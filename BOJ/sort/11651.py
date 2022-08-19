
import sys

n=int(sys.stdin.readline())
a=[]
for i in range(n):

    b=[int(j) for j in sys.stdin.readline().split(" ")]
    a.append(b[-1::-1])
a.sort()

for x,y in a:
    print(y,x)

