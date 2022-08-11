import string


for i in range(int(input())):
    strings = list(input().split())
    
    answer=''
    for x in str(strings[1]):
       
        answer=answer+x*int(strings[0])

    print(answer)

    