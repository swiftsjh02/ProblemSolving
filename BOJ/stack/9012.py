line = int(input())

for i in range(line):
    stack=[]
    temp=input()
    for k in temp:
        if k=='(':
            stack.append(k)
        elif k==')':
            if len(stack)!=0:
                stack.pop
            else:
                print("NO")
                break
    else:
        if len(stack)==0:
            print("YES")
        else:
            print("NO")
