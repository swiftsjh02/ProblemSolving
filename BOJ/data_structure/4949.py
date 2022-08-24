while True:
    big=[]
    
    sentence=input()
    if sentence[0]=='.':
        break
    for c in sentence:
        if c=='[':
            big.append(c)
        if c=='(':
            big.append(c)
            
            
        if c==']' or c==')':
            if c==')':
                if big.pop()=='(':
                    pass
                elif big.pop()=='[':
                    print("no")
                    break
            elif c==']':
                if big.pop()=='[':
                    pass
                elif big.pop()==')':
                    print("no")
                    break

        if c=='.':
            break
    print(big)
    if len(big)==0:
        print("yes")
    continue