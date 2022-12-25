#include<stdio.h>
#include<stdlib.h>


void dfs(int **graph,int* visited,int n,int v){
    visited[v]=1;
    for(int i=0; i<n; i++){
        if(graph[v][i]==1 && visited[i]==0){
            dfs(graph,visited,n,i);
        }
    }
    return;
    
}

int main(){
    int n,m,cnt=0;
    scanf("%d %d",&n,&m);
    int **graph=malloc(sizeof(int*)*n);
    for(int i=0; i<n; i++){
        graph[i]=malloc(sizeof(int)*n);
    }

    int *visited=malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        visited[i]=0;
    }


    for(int i=0; i<m; i++){
        int u,v=0;
        scanf("%d %d",&u,&v);
        graph[u-1][v-1]=1;
        graph[v-1][u-1]=1;
    
    }

    for(int i=0; i<n; i++){
        if(visited[i]==0){
            dfs(graph,visited,n,i);
            cnt+=1;
        }
    }

    printf("%d",cnt);



    return 0;
}