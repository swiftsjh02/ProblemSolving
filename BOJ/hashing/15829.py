input()
line=input()
answer=0

for i in range(0,len(line)):
    answer=answer+int(ord(line[i])-96)*31**i

print(answer%1234567891)
