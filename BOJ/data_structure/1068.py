
def dfs(num,arr):
    arr[num]=-2

    for i in range(len(arr)):
        if num==arr[i]:
            dfs(i,arr)


input()
insertion=[int(k) for k in input().split()]
k=int(input())
count=0


dfs(k,insertion)

for i in range(len(insertion)):
    if insertion[i]!=-2 and i not in insertion:
        count+=1

#print(insertion)
print(count)


    

