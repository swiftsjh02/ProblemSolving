a=[int(j) for j in input().split()]
state=set()
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        state.add("ascending")
    else:
        state.add("descening")


if(len(state))==2:
    print("mixed")
else:
    print(state.pop())
    