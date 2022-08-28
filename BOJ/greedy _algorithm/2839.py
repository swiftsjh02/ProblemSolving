


N=int(input())


count=0
tmp=N
while True:
    count+=tmp//5
    tmp=tmp%5
    if tmp%3==0:
        count+=tmp//3
        print(count)
        break
    else:
        tmp=N
        count=0
        loop=tmp//5
        for i in range(loop,-1,-1):
            
            tmp=N
            count+=i
            tmp=tmp-5*i
            
            if tmp%3==0:
                count+=tmp//3
                print(count)
                quit()
            else:
                count=0
        
    print("-1")
    break