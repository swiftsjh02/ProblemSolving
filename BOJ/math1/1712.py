a=input().split(" ")

stdcost=int(a[0])
perone=int(a[1])
persell=int(a[2])

if persell<=perone:
    print(-1)
    quit()

print(int(stdcost/(persell-perone)+1))


