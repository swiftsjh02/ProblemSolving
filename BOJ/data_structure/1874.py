n=int(input())
answer=[]
for i in range(n):
    answer.append(int(input()))

stack=[]
answer2=[]
plus_minus=[]
i=0
while True:

    

    try:
        while stack[len(stack)-1]==answer[0]:
            answer.remove(answer[0])
            answer2.append(stack.pop())
            plus_minus.append("-")
            if len(answer2)==n:
                break

    except:
        pass


    if len(answer2)==n:
        break
    i+=1
    stack.append(i)
    plus_minus.append("+")

    if i==n:
        tmp=list(reversed(stack))
        if tmp!=answer:
            print("NO")
            quit()
    


for i in plus_minus:
    print(i)
    
    
    
        
   

    
    
    
  
    
    
