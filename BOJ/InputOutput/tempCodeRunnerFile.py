


a=input()
temp=a
i=0
while True:
    i+=1
    temp=str(temp[1:2])+str( (int(temp[0:1])+int(temp[1:2]))%10 )

    if temp==a:break

print(i)