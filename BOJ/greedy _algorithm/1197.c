#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int prim(int **matrix,int n,int*node){
    int start=0;
    int *visited=(int*)malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        visited[i]=0;
    }
    visited[0]=1;
    int distance=0;

    for(int i=0; i<n-1; i++){
        int min=100000000;
        int next=-1;

        for(int v=0; v<n; v++){
            if(visited[v]==1){
                for(int j=0; j<n; j++){
                    if(visited[j]==0){
                        if(matrix[v][j]<min){
                            min=matrix[v][j];
                            next=j;
                        }
                    }
                }
            }
        }
        visited[next]=1;
        distance+=min;
    }
    return distance;
}



int main(){
   
    int v,e;
    scanf("%d %d",&v,&e);
    int **input=(int**)malloc(sizeof(int*)*e);
    for(int i=0; i<e; i++){
        input[i]=(int*)malloc(sizeof(int)*3);
    }
   
    int *node=(int *)malloc(e*sizeof(int));
    for(int i=0; i<e; i++){
        scanf("%d %d %d",input[i],input[i]+1,input[i]+2);
    }
    
    

    printf("%d\n",prim(matrix,e,node));


    return 0;
}