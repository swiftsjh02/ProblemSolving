samp=[1,1,2,2,2,8]
answer=list()
temp=[int(i) for i in input().split(" ")]



for a,b in zip(samp,temp):
    print(a-b,end=" ")
    