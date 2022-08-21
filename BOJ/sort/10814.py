
a=[]
for i in range(int(input())):
   tmp=[k for k in input().split()]
   a.append(tmp)


a.sort(key = lambda x: int(x[0]))
for i in a:
    print(i[0],i[1])