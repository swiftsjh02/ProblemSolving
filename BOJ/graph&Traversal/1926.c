#include<stdio.h>
#include<stdlib.h>

int max=0;
int tmp=0;
int n,m=0;
int cnt=0;


int dfs_R(int x,int y,int**visit,int**graph){
    if(x>=n||x<=-1||y<=-1||y>=m){
        return 0;
    }

    if(visit[x][y]==0&&graph[x][y]==1){
        visit[x][y]=1;
        tmp+=1;
        dfs_R(x-1,y,visit,graph);
        dfs_R(x,y-1,visit,graph);
        dfs_R(x+1,y,visit,graph);
        dfs_R(x,y+1,visit,graph);
        return 1;
    }
    return 0;
}

int main(){
    
    scanf("%d %d",&n,&m);
    int **graph=malloc(sizeof(int*)*n);
    int **visit=malloc(sizeof(int*)*n);
    for(int i=0; i<n; i++){
        visit[i]=malloc(sizeof(int)*m);
        graph[i]=malloc(sizeof(int)*m);
    }
   
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%d",&graph[i][j]);
            visit[i][j]=0;
        }
       
    }
    

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(visit[i][j]==0){
                if(dfs_R(i,j,visit,graph)==1){
                    if(tmp>max){
                        max=tmp;
                    }
                    tmp=0;
                    cnt+=1;
                }
            }
        }
    }

    printf("%d\n%d",cnt,max);

    


}

