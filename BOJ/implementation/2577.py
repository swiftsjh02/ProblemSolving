a=int(input())
b=int(input())
c=int(input())
answer=a*b*c
answer=str(answer)
oh=[0,0,0,0,0,0,0,0,0,0]
for k in answer:
    
    oh[int(k)]+=1

for k in oh:
    print(k)