from pprint import pprint
import sys

sys.setrecursionlimit(1000000)

def editD(a,b):
    for i,charB in enumerate(b,start=1):
        for j,charA in enumerate(a,start=1):
            if charA == charB: # If the characters are the same
                dp[i][j]=dp[i-1][j-1]+1
            else: # if the characters are different
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
    return dp[-1][-1] #return minimal edit distance

def check(i,j):


    if dp[i][j]==0:
        return

    if dp[i][j]==dp[i-1][j]:
        check(i-1,j)
    elif dp[i][j]==dp[i][j-1]:
        check(i,j-1)
    else:
        result.append(a[j-1])
        check(i-1,j-1)
    pass

  
a=input()
b=input()

dp=[[0 for i in range(len(a)+1)] for j in range(len(b)+1)] #make dp table
result=[]
for i in range(1,len(b)+1): #initialize first row
    dp[i][0]=0
for i in range(1,len(a)+1): #initialize first column
    dp[0][i]=0

ans=editD(a,b)



if ans==0:
    print(ans)
else:
    check(len(b),len(a))
    print(ans)
    print(''.join(result[::-1]))



