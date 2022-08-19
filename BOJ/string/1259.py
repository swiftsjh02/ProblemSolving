while True:
    a=[int(k) for k in input()]
    if a[0]==0:
        break

    if a==a[-1::-1]:
        print("yes")
    else:
        print("no")
    
 
