

import sys

rope=[]
for i in range(int(sys.stdin.readline())):
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)


for i in range(len(rope)):
    rope[i]=rope[i]*(i+1)

print(max(rope))