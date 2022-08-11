n=int(input())
for i in range(n):
    t=0
    z=0
    for x in input():
        if x=='O':
            z+=1
            t=t+z
        elif x=='X':
            z=0
    
    print(t)
