nums=set()
input()
match=dict()
for k in input().split(" "):
    if int(k) in nums:
        match[int(k)]+=1
    else:
        nums.add(int(k))
        match[int(k)]=1
input()
for k in input().split(" "):
    if int(k) in nums:
        print(match[int(k)],end=" ")
    else:
        print("0",end=" ")