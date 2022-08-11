


n=int(input())
for i in range(n):
    avg=0
    overavg=0
    strings = list(map(int,input().split()))

    avg=sum(strings[1:])/strings[0]
    for score in strings[1:]:
        if score>avg:
            overavg+=1
        
    


    
    print("{:.3f}%".format(overavg/strings[0]*100))




           
        

