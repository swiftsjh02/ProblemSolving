#include <stdio.h>
#include <stdlib.h>


int cost=0;

void printsolution(int path[],int V){
    int i;
    for(i=0;i<V;i++){
        printf("%d ",path[i]);
    }
    printf("%d ",path[0]);
    printf("\n");
}

bool isSafe(int v, int **graph, int path[], int pos){
    if(graph[path[pos-1]][v]==0)
        return false;
    for(int i=0;i<pos;i++){
        if(path[i]==v)
            return false;
    }
    return true;
}

bool hamcycleutil(int **graph, int path[], int pos,int V){
    if(pos==V){
        if(graph[path[pos-1]][path[0]]!=0){
            cost+=graph[path[pos-1]][path[0]];
            return true;
            }
        else
            return false;
    }
    for(int v=1;v<V;v++){
        if(isSafe(v,graph,path,pos)){
            path[pos]=v;
            cost+=graph[path[pos-1]][path[pos]];
            if(hamcycleutil(graph,path,pos+1,V)==true)
                return true;
            path[pos]=-1;
        }
    }
    return false;
}

bool hamcycle(int **graph, int V){
    int *path=new int[V];
    for(int i=0;i<V;i++)
        path[i]=-1;
    path[0]=0;
    if(hamcycleutil(graph,path,1,V)==false){
        printf("Solution does not exist\n");
        return false;
    }
    printsolution(path,V);
    return true;
}




int main(){
    int V;
    int n,m;
    scanf("%d %d",&n,&m);
    V=n-1;
    //2D array size of V*V
    int **graph=(int **)malloc(V*sizeof(int *));
    for(int i=0;i<V;i++){
        graph[i]=(int *)malloc(V*sizeof(int));
    }
    for(int i=0; i<V; i++){
        for(int j=0; j<V; j++){
            graph[i][j]=0;
        }
    }
    for(int i=0; i<m; i++){
        int u,v;
        scanf("%d %d",&u,&v);
        graph[u-1][v-1]=1;
    }

    
    hamcycle(graph,V);
    printf("%d",cost);
    return 0;
}