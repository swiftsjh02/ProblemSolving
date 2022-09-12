import sys

n,m,b=map(int,sys.stdin.readline().split())
maps=list()

answer=999999999
level=0
for i in range(n):
    tmp=list(map(int,sys.stdin.readline().split()))
    maps.append(tmp)



for mapmin in range(257):

    use=0
    take=0
    time_tmp=0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]-mapmin>=0:
                take+=maps[i][j]-mapmin
            else:
                use+=mapmin-maps[i][j]

    if use>take+b:
        continue

    time_tmp=take*2+use

    if time_tmp<=answer:
        answer=time_tmp
        level=mapmin

    
                    

print(answer,level)