for i in range(int(input())):
    coins=[25,10,5,1]
    money=int(input())
    count=[]
    for coin in coins:
        count.append(money//coin)
        money=money%coin
    
    for c in count:
        print(c,end=" ")
    print()
    
    