n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            arr[i][j]=float('inf')



for l in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                arr[i][j]=1
            arr[i][j]=min(arr[i][j],arr[i][l]+arr[l][j])

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]!=float('inf'):
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()