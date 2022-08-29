from collections import deque

for i in range(int(input())):

    n,m=map(int,input().split())
    queue=deque([int(k) for k in input().split()]) # 9 7 2 5 8 1       
    print_count=1
    index=m

    while len(queue)!=0:
        
        tmp=queue.popleft()
        try:
            if max(queue)>tmp:
                queue.append(tmp)   
                index-=1
                if index<0:
                    index=len(queue)-1

            else:
                if index==0:
                    print(print_count)
                    break
                else:
                    print_count+=1
                    index-=1
                
        except:
            if index==0:
                print(print_count)
                break


