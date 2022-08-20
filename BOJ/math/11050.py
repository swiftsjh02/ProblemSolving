def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)



a=[int(k) for k in input().split(" ")]

up=fact(a[0])

down=fact(a[0]-a[1])*fact(a[1])

print(int(up/down))




