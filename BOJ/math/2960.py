def calculate(n,k):
    num=[]
    deleted=[]
    for i in range(2,n+1):
        num.append(i)
    while allmimus(num)==False:
        small=smallest(num)
        for i in range(len(num)):
            if num[i]%small==0:
                deleted.append(num[i])
                num[i]=-1
                
    print(deleted[k-1])
def smallest(num):
    s=float('inf')
    for i in num:
        if i<s and i!=-1:
            s=i
    return s
def allmimus(num):
    a=True
    for i in num:
        if i!=-1:
            return False
    return True
n,k=map(int,input().split())
calculate(n,k)

