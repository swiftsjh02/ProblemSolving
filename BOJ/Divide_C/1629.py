def power(n,k):
    if k==1:
        return n%C

    
    x=power(n,k//2)

    if n%2==0:
        return x*x%C
    else:
        return x*x*n%C


A,B,C=map(int,input().split())

print(power(A,B)%C)