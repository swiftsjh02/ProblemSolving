answer=0
for k in input().split(" "):
    answer=answer+int(k)**2

print(answer%10)