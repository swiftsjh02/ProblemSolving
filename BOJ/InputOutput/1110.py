


origin=int(input())
temp=origin
i=0
while True:
     a = temp//10
     b = temp%10
     c = (a+b)%10
     temp=(b*10)+c

     i=i+1
     if temp==origin:
        break

print(i)
