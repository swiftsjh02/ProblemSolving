

for l in range(int(input())):

    k=int(input())
    n=int(input())

    save=[k,n]

    apartment=[]
    apartment.append([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    for i in range(k):
        tmp=[]
        for j in range(14):
            tmp2=0
            for k in range(0,j+1):
                tmp2+=apartment[i][k]
            tmp.append(tmp2)
        apartment.append(tmp)



    print(apartment[save[0]][save[1]-1])

            

