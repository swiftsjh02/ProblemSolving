matching=["c=","c-","dz=","d-","lj","nj","s=","z="]
line=input()


for x in matching:
    line=line.replace(x,"@")
print(len(line))
        
