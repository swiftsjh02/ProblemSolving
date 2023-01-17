n=int(input())
seminar=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    tmp.append(tmp[1]-tmp[0])
    seminar.append(tmp)

seminar.sort(key= lambda x:(x[1],x[0],x[2]))


cnt=1
endtime=seminar[0][1]
for i in range(1,len(seminar)):
    
    if endtime>seminar[i][0]:
        pass
    else:
        endtime=seminar[i][1]
        cnt+=1

print(cnt)
