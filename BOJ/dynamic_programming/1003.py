

def fibo(n):
    if n == 0:
        return [1, 0]
    if n == 1:
        return [0, 1]
    if fibolist[n]!=[0, 0]:
        return fibolist[n]
    fibolist[n]=[fibo(n-1)[0]+fibo(n-2)[0], fibo(n-1)[1] + fibo(n-2)[1]]
    return fibolist[n]
    


case = int(input())
for i in range(case):
    n=int(input())
    fibolist=[[0,0] for i in range(n+1)] #count for 0, count for 1
    res = fibo(n)
    print(res[0], res[1])
