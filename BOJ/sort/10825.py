n=int(input())
score=[]
for i in range(n):
    n,a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    score.append([n,a,b,c])

score.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in score:
    print(i[0])