
import sys
sys.setrecursionlimit(10000)
def fibo(n):
    
    if n<=2:
        return 1
    if fibolist[n]!=0:
        return fibolist[n]
    fibolist[n]=fibo(n-1)+fibo(n-2)
    return fibolist[n]
    



n=int(input())
fibolist=[0]*(n+1)


print(fibo(n))