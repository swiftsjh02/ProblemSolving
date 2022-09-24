from pprint import pprint


def divide(arr):

    if len(arr)==1:
        return arr[0][0]

    if arr[0][0]==0:
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j]==1:
                    cutleftup=[]
                    for i in range(len(arr)//2):
                        tmp=[]
                        for j in range(len(arr[0])//2):
                            tmp.append(arr[i][j])
                        cutleftup.append(tmp)
                    
                    cutrightup=[]
                    for i in range(len(arr)//2):
                        tmp=[]
                        for j in range(len(arr[0])//2,len(arr[0])):
                            tmp.append(arr[i][j])
                        cutrightup.append(tmp)
                    divide(cutrightup)

                    cutleftdown=[]
                    for i in range(len(arr)//2,len(arr)):
                        tmp=[]
                        for j in range(len(arr[0])//2):
                            tmp.append(arr[i][j])
                        cutleftdown.append(tmp)
                    divide(cutleftdown)

                    cutrightdown=[]
                    for i in range(len(arr)//2,len(arr)):
                        tmp=[]
                        for j in range(len(arr[0])//2,len(arr[0])):
                            tmp.append(arr[i][j])
                        cutrightdown.append(tmp)
                    divide(cutrightdown)
        
    
    elif arr[0][0]==1:
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j]==0:
                    cutleftup=[]
                    for i in range(len(arr)//2):
                        tmp=[]
                        for j in range(len(arr[0])//2):
                            tmp.append(arr[i][j])
                        cutleftup.append(tmp)
                    
                    cutrightup=[]
                    for i in range(len(arr)//2):
                        tmp=[]
                        for j in range(len(arr[0])//2,len(arr[0])):
                            tmp.append(arr[i][j])
                        cutrightup.append(tmp)
                    divide(cutrightup)

                    cutleftdown=[]
                    for i in range(len(arr)//2,len(arr)):
                        tmp=[]
                        for j in range(len(arr[0])//2):
                            tmp.append(arr[i][j])
                        cutleftdown.append(tmp)
                    divide(cutleftdown)

                    cutrightdown=[]
                    for i in range(len(arr)//2,len(arr)):
                        tmp=[]
                        for j in range(len(arr[0])//2,len(arr[0])):
                            tmp.append(arr[i][j])
                        cutrightdown.append(tmp)
                    divide(cutrightdown)

    answer.append(arr[0][0])
                



    
    




    

    

answer=[]
n=int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int,input(""))))

pprint(arr)

divide(arr)


print(answer)







    

