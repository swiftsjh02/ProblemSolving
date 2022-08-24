while True:
    big=[]
    small=[]
    sentence=input()
    if sentence[0]=='.':
        break
    for c in sentence:
        if c=='[':
            big.append(c)
        if c==']':
            try:
                big.pop()
            except:
                print("no")
        if c=='(':
            small.append(c)
        if c==')':
            try:
                small.pop()
            except:
                print("no")
        if c=='.':
            break

    if len(big)==0 and len(small)==0:
        print("yes")
    continue
    

    