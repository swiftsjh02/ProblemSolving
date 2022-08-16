while True:
    a=[int(k) for k in input().split(" ")]
    if a[0] == 0 and a[1] == 0:
        break
    elif a[0] or a[1] != 0:
        print(a[0]+a[1])