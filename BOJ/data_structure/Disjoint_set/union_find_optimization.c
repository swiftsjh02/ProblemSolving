#include<stdio.h>
#include<stdlib.h>

int n=5;
int parent[n];
int rank[n];

int find(int u) {
    if(u == parent[u])
        return u;
    
    // parent를 찾아낸 루트로 아예 바꿔버리면
    // find 연산 수행시 중복되는 연산을 줄여준다.
    // 재귀적인 구현 덕분에 u에서 루트까지 올라가는 경로상에 있는
    // 모든 노드들에게도 경로 압축 최적화가 자동으로 수행된다.
    return parent[u] = find(parent[u]);
}


void union(int u, int v) {
    u = find(u);
    v = find(v);
    
    if(u == v) return;
    
    if(rank[u] > rank[v])
        swap(u, v);
    
    parent[u] = v;
    
    // 두 트리의 높이가 같은 경우에는 결과 트리의 rank를 1 증가시킨다.
    if(rank[u] == rank[v]){
     rank[v]++;
}

int main(){


for(int i = 0; i < n; i++)
    parent[i] = i;
    
for(int i = 0;i < n; i++) 
    rank[i] = 1;

    }





