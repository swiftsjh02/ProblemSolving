from pprint import pprint
import sys

sys.setrecursionlimit(100000)

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def check(paper,lefttop,rightbottom):
    global white,blue
    color = paper[lefttop.y][lefttop.x]
    
        


    for i in range(lefttop.x,rightbottom.x+1):
        for j in range(lefttop.y,rightbottom.y+1):
            if paper[j][i]!=color:
                lefttop1=point(lefttop.x,lefttop.y)
                rightbottom1=point((lefttop.x+rightbottom.x)//2,(lefttop.y+rightbottom.y)//2)
                lefttop2=point(lefttop.x,(lefttop.y+rightbottom.y)//2+1)
                rightbottom2=point((lefttop.x+rightbottom.x)//2,rightbottom.y)
                lefttop3=point((lefttop.x+rightbottom.x)//2+1,lefttop.y)
                rightbottom3=point(rightbottom.x,(lefttop.y+rightbottom.y)//2)
                lefttop4=point((lefttop.x+rightbottom.x)//2+1,(lefttop.y+rightbottom.y)//2+1)
                rightbottom4=point(rightbottom.x,rightbottom.y)
                check(paper,lefttop1,rightbottom1)
                check(paper,lefttop2,rightbottom2)
                check(paper,lefttop3,rightbottom3)
                check(paper,lefttop4,rightbottom4)
                return
    if color==0:
        white+=1
    else:
        blue+=1
    
            

    


n=int(input())
paper=[]
for i in range(n):
    paper.append(list(map(int,input().split())))

white=0
blue=0
check(paper,point(0,0),point(n-1,n-1))
print(white)
print(blue)



