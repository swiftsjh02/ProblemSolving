

while True:
    a=[int(k) for k in input().split(" ")]
    a.sort()
  
    
    if int(a[0])==0:
        break

    if int(a[0])**2+int(a[1])**2==int(a[2])**2:
        print("right")
    else:
        print("wrong")