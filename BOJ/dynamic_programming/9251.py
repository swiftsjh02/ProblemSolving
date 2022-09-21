from pprint import pprint

def editD(a,b):
    for i,charB in enumerate(b,start=1):
        for j,charA in enumerate(a,start=1):
            if charA == charB: # If the characters are the same
                dp[i][j]=dp[i-1][j-1]+1
            else: # if the characters are different
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
    return dp[-1][-1] #return minimal edit distance
  
a=input()
b=input()

dp=[[0 for i in range(len(a)+1)] for j in range(len(b)+1)] #make dp table
for i in range(1,len(b)+1): #initialize first row
    dp[i][0]=0
for i in range(1,len(a)+1): #initialize first column
    dp[0][i]=0

print(editD(a,b))

for i in range(len(b)+1):
    print(dp[i])









