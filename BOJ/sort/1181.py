
words=[]
max_len=0
for i in range(int(input())):
    tmp=input()
   
    if tmp not in words:
        words.append(tmp)

words.sort(key= lambda x:(len(x),x))

for word in words:
    print(word)