
import pprint


n=int(input()) ##노드의 개수
e=int(input()) ##엣지의 개수
arr=[[float('inf') for i in range(n)] for i in range(n)] ## 거리배열 초기화 
for i in range(n):
    for j in range(n):
        if i==j: # i와 j 가 같으면 i->i 노드의 거리라는 의미와 같아서 자기 자신과의 거리는 0
            arr[i][j]=0
input=[list(map(int,input().split())) for i in range(e)]

for e in input:
    arr[e[0]-1][e[1]-1]=min(e[2],arr[e[0]-1][e[1]-1])



for l in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            arr[i][j]=min(arr[i][j],arr[i][l]+arr[l][j])# 기존의 값과 l 노드를 지나서 가는 경우의 값을 비교 최소 값으로 갱신


#여기까지 하면 arr 테이블의 거리는 최소 거리 갱신이 완료됨 

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]==float('inf'):
            print(0,end=' ')
        else:
            print(arr[i][j],end=' ')
    print()





