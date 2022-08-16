


counters={}
for k in input():
    if k.upper() in counters:
        counters[k.upper()]+=1
    else:
        counters[k.upper()]=1



    
max=0
max_a=''

for k,j in counters.items():
  
    if max<j:
        max=j
        max_a=k
cnt=0
for k in counters.values():
    if k==max:
        cnt+=1
    
    if cnt>1:
        print("?")
        quit()
    

print(max_a)



