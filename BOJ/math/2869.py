import math

a,b,v=map(int,input().split())


if math.floor(v//a)==1:
    print(1)
else:
    print(math.ceil((v-b)/(a-b)))