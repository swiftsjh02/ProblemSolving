

def fibo1(n):
   
   
    if n<=2:
        return 1
    else:
        return fibo1(n-1)+fibo1(n-2)

def fibo2(n):
    global b
    global fibolist
    

    if fibolist[n]!=0:
        return fibolist[n]

    if n<=2:
       return 1

    b+=1   
    fibolist[n]=fibo2(n-1)+fibo2(n-2)
    return fibolist[n]




b=0
n=int(input())
fibolist=[0]*(n+1)
fibo1(n)
fibo2(n)

print(fibo1(n),b)
