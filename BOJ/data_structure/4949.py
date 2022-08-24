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
            
            
        if c==']':
          if len(big)!=0 and big[-1] =='[':
            big.pop()
          else:
            big.append(']')
        if c==')':
          if len(big)!=0 and big[-1] =='(':
            big.pop()
          else:
            big.append(')')
            

    if len(big)==0:
        print("yes")
    else:
        print("no")


    continue