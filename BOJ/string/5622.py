matching = {"ABC":3,"DEF":4,"GHI":5,"JKL":6,"MNO":7,"PQRS":8,"TUV":9,"WXYZ":10}
answer=0
for x in input():
    for temp in matching.keys():
        if x in temp:
            answer+=matching.get(temp)

print(answer)
