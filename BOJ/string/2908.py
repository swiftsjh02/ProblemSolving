max=0
for x in input().split(" "):
    if int(x[-1::-1])>max:
        max=int(x[-1::-1])

print(max)