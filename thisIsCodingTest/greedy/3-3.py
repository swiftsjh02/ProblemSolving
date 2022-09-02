n,m=map(int,input().split())
answer=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    answer.append(min(tmp))

print(max(answer))
