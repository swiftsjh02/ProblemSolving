a=input().split(" ")
cards=input().split(" ")
listofcard=[]
for i in range(int(a[0])):
    for j in range(i+1,int(a[0])):
        for k in range(j+1,int(a[0])):
            
            if int(cards[i])+int(cards[j])+int(cards[k])<=int(a[1]):
                listofcard.append(int(cards[i])+int(cards[j])+int(cards[k]))



print(max(listofcard))
