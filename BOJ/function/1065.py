def hansu(n):
    cnt=0
    for i in range(1,n+1):
        if i<100:
            cnt+=1
        elif i>=100:
            num=[k for k in map(int,str(i))]
            if num[2]-num[1]==num[1]-num[0]:
                cnt+=1
    return(cnt)
        

print(hansu(100))