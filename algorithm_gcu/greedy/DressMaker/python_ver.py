n=4
time=[3,1,2,5]
fine=[4,1000,2,5]
ans=[0,1,2,3]
for i in range(n):
    for j in range(n-1):
        if time[ans[j]]*fine[ans[j+1]]>time[ans[j+1]]*fine[ans[j+1]]:
            ans[j],ans[j+1]=ans[j+1],ans[j]
        elif(time[ans[j]]*fine[ans[j+1]]==time[ans[j+1]]*fine[ans[j+1]]):
            if ans[j]>ans[j+1]:
                ans[j],ans[j+1]=ans[j+1],ans[j]
        


for i in ans:
    print(i+1,end=' ')