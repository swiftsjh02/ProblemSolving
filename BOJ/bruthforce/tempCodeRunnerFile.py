
import pprint



def check(board):
    idx1=0
    idx2=0
    cnt=[]
    for a in range(8):
        for b in range(8):
            if (a+b)%2==0:
                if board[a][b]!="W":idx1+=1
                if board[a][b]!="B":idx2+=1
            else:
                if board[a][b]!="B": idx+=1
                if board[a][b]!="W": idx2+=1
    cnt.append(idx1)
    cnt.append(idx2)
    return min(cnt)
        


n,m=map(int,input().split())
board=[]
for i in range(n):
    board.append(input())



cut=[]
for l in range(n-7):
    
    for k in range(m-7):
        tmp=[]
        for j in range(0,8):
            tmp.append(board[j+l][0+k:8+k])
        cut.append(tmp)
   




answer=[]
for i in range(0,len(cut)):
   
    answer.append(check(cut[i]))

print(min(answer))

