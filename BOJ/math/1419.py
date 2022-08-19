import sys
import time

l=int(sys.stdin.readline())
r=int(sys.stdin.readline())
k=int(sys.stdin.readline())

start = time.time()

max=1000000
s1=set()
for x in range(1,max):
    for d in range(1,max):
        answer=k*x+(k**2*d-k*d)/2
        
     
        if answer>=l and answer<=r:
            s1.add(answer)
            print("x: "+str(x)+" d:"+str(d)+" answer:"+str(answer))
        elif answer>r:
            break
        


print(len(s1))

print("time: ",time.time()-start)
