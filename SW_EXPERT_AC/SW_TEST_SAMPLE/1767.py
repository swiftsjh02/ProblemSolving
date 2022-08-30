arr=[]

n=int(input())

for i in range(n):
    tmp=list(map(int,input()))


def search(x,y):
    if arr[x][y]==0:
        return False
    else:
        try:
            arr[x][y+1]
            arr[x][y-1]
            arr[x-1][y]
            arr[x+1][y]
        except:
            pass


for i in range(n):
    for j in range(n):
        search(i,j)



