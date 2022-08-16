def selfnum(k):
    answer=0
    k=str(k)
    for i in k:
        answer=answer+int(i)
    answer=answer+int(k)
    return(answer)
        

a=list()

for i in range(1,10001):
    if selfnum(i)<10001:
        a.append(selfnum(i))
        
for i in range(1,10001):
    if i not in a:
        print(i)
        