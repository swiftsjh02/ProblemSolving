

#make find max function
def find_max(cake):
    max=0
    for i in range(len(cake)):
        if cake[i]>max:
            max=cake[i]
    return max

#make function that check list is sorted
def is_sorted(cake):
    for i in range(len(cake)-1):
        if cake[i]>cake[i+1]:
            return False
    return True

#make function that flip list from index as parameter
def flip(cake,index):

    if index==0:
        return cake
    answer.append(index+1)
    cake[:index+1]=reversed(cake[:index+1])
    return cake




for i in range(int(input())):

    #input number of element and list
    tmp=list(map(int,input().split()))
    cake=tmp[1:]


    lastidx=len(cake)-1
    answer=[]
    while not is_sorted(cake):

        (flip(cake,cake.index(find_max(cake))))
        (flip(cake,len(cake)-1))
        lastidx-=1
        cake=cake[0:lastidx+1]
        
        
    
    print(len(answer),end=" ")
    for i in answer:
        print(i,end=" ")
    print()
