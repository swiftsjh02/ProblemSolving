n=int(input())
arr=list(map(int,input().split()))

dp=list()


for arr_e in arr:
    if len(dp)==0:
        dp.append(arr_e)
    else:
        if dp[-1]<arr_e:
            dp.append(arr_e)
        else:
            for i in range(len(dp)):
                if dp[i]>=arr_e:
                    dp[i]=arr_e
                    break

print(len(dp))
    