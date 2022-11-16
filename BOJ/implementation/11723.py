import sys

sets=set()

for _ in range(int(sys.stdin.readline())):
    commd=list(sys.stdin.readline().split())

    if len(commd)==1:
        if commd[0]=='all':
            sets=set([i for i in range(1,21)])
        else:
            sets=set()

    else: 
        if commd[0]=="add":
            sets.add(int(commd[1]))
        elif commd[0]=="remove":
            if commd[1] in sets:
                sets.discard(commd[1])
            
        elif commd[0]=="check":
            if commd[1] in sets:
                print(1)
            else:
                print(0)
        elif commd[0]=="toggle":
            if commd[1] in sets:
                sets.discard(commd[1])
            else:
                sets.add(int(commd[1]))
    