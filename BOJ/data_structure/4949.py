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
                try:
                    tmp=big.pop()
                except:
                    print("no")
                    big.append("no")
                    break
                if tmp=='(':
                    pass
                elif tmp=='[':
                    print("no")
                    big.append("no")
                    break
            elif c==']':
                try:
                    tmp=big.pop()
                except:
                    print("no")
                    big.append("no")
                    break
                if tmp=='[':
                    pass
                elif tmp=='(':
                    print("no")
                    big.append("no")
                    break

    if len(big)==0:
        print("yes")
        continue