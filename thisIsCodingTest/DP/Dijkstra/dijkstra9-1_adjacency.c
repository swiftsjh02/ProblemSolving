#include <stdio.h>
#include <stdlib.h>

int main(){
    int v,e,k=0;
    scanf("%d %d",&v,&e);
    scanf("%d",&k);
    int **adjacency = (int**)malloc(sizeof(int*)*v);
    int *visited = (int*)malloc(sizeof(int)*v);
    int *distance = (int*)malloc(sizeof(int)*v);
    for(int i=0;i<v;i++){
        adjacency[i] = (int*)malloc(sizeof(int)*v);
        for(int j=0;j<v;j++){
            adjacency[i][j] = 0;
        }
    }

    for(int i=0; i<v; i++){
        visited[i] = 0;
        distance[i] = 100000000;
    }

    visited[k-1] = 1;
    distance[k-1] = 0;

    for(int i=0;i<e;i++){
        int a,b,c=0;
        scanf("%d %d %d",&a,&b,&c);
        adjacency[a-1][b-1] = c;
    }

    for(int i=0;i<v;i++){
        for(int j=0;j<v;j++){
            printf("%d ",adjacency[i][j]);
        }
        printf("\n");
    }

    for(int i=0; i<v-1; i++){
        int min=100000000;
        int min_index=0;
        for(int j=0; j<v; j++){
            if(visited[j] == 0 && distance[j] < min){
                min = distance[j];
                min_index = j;
            }
        }
        visited[min_index] = 1;
        for(int j=0; j<v; j++){
            if(visited[j] == 0 && adjacency[min_index][j] != 0){
                if(distance[j] > distance[min_index] + adjacency[min_index][j]){
                    distance[j] = distance[min_index] + adjacency[min_index][j];
                }
            }
        }

    }

    for(int i=0; i<v; i++){
        printf("%d\n",distance[i]);
    }



}