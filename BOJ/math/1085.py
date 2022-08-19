num=[int(k) for k in input().split(" ")]
x=num[0]
y=num[1]
w=num[2]
h=num[3]

print(min(h-y,y,x,w-x))