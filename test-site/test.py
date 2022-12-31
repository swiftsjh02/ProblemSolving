n=input()
a=[]
for i in n:
    if ord(i)<97:
        a.append(i.lower())
    else:
        a.append(i.upper())

for i in a:
    print(i,end="")