import math

n=int(input())
count=0
str1=math.factorial(n)





str1=str(str1)
str1=str1[-1::-1]
i=0
while True:
    if str1[i]!='0':
        break
    
    count+=1
    i+=1

        
print(count)