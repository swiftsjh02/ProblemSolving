n=int(input())
array=[]
ans=[[0]*3 for i in range(n+1)]
for i in range(n):
    tmp=list(map(int,input().split()))
    array.append(tmp)
for i in range(1,n+1):
    ans[i][0]=min(ans[i-1][1],ans[i-1][2])+array[i-1][0]
    ans[i][1]=min(ans[i-1][0],ans[i-1][2])+array[i-1][1]
    ans[i][2]=min(ans[i-1][0],ans[i-1][1])+array[i-1][2]

print(min(ans[n][0],ans[n][1],ans[n][2]))