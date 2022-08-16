import sys
a=[]
for k in sys.stdin.readline():
   a.append(int(k))

a.sort(reverse=True)
for k in a:
    print(k,end="")