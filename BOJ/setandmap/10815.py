import sys

a=set()

sys.stdin.readline()
a=set(map(int,sys.stdin.readline().split(" ")))




sys.stdin.readline()
b= list(map(int,sys.stdin.readline().split(" ")))

for i in b:
    if i in a:
        print(1,end=" ")
    else:
        print(0,end=" ")



print("\b")
