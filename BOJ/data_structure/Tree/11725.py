import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
#인접 리스트 방식의 표현
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

arr = []

def dfs(s):
    for i in graph[s]: ##s랑 연결된 노드들 중에서
        if visited[i] == 0:#방문하지 않았다면
            visited[i] = s #방문하지 않은 노드의 인덱스 부분을 부모(s)로 기록
            dfs(i) # i랑 연결된 노드 찾기

dfs(1) #루트에서 시작

for x in range(2, n+1):
    print(visited[x]) ## 각각의 부모가 기록된 배열 출력