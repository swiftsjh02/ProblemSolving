def fibo(n):
    if n == 0:
        return [1, 0]
    if n == 1:
        return [0, 1]
    if fibolist[n]!=[0, 0]:
        return fibolist[n]
    fibolist[n]=[fibo(n-1)[0]+fibo(n-2)[0], fibo(n-1)[1] + fibo(n-2)[1]]
    return fibolist[n]

def generalfibo(n):
    global cnt
    cnt+=1
    if n<=2:
        return 1
    else:
        return generalfibo(n-1)+generalfibo(n-2)

n=int(input())
cnt=0
fibolist=[[0,0] for i in range(n+1)]
generalfibo(n)
print(fibo(n)[1])