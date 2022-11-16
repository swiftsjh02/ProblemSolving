#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int bellman_ford(int **graph,int n,int source){
    int max=-1;
    int maxindex=-1;
    int i,j;
    int *distance=(int *)malloc(n*sizeof(int));
    for(i=0;i<n;i++){
        distance[i]=1000000000;
    }
    distance[source]=0;
    for(i=0;i<n-1;i++){
        for(j=0;j<n;j++){
            if(distance[j]!=1000000000){
                int k;
                for(k=0;k<n;k++){
                    if(graph[j][k]!=0){
                        if(distance[k]>distance[j]+graph[j][k]){
                            distance[k]=distance[j]+graph[j][k];
                        }
                    }
                }
            }
        }
    }
    for(i=0;i<n;i++){
        if(distance[i]>max){
            max=distance[i];
            maxindex=i;
        }
    }
    return maxindex+1;
}

int main(){
    FILE *fp= fopen("input.txt","r");
    int f,i;
    fscanf(fp,"%d %d",&f,&i);
    //printf("number of health center: %d\n",f);
    //printf("number of intersection: %d\n",i);
    int *healthcenter=malloc(sizeof(int)*(f));
    int **intersection=malloc(sizeof(int *)*(i));
    for(int j=0;j<i;j++){
        intersection[j]=malloc(sizeof(int)*(i));
    }
    for(int i=0; i<f; i++){
        int tmp;
        fscanf(fp,"%d",&tmp);
        tmp--;
        healthcenter[i]=tmp;
        //printf("healthcenter: %d\n",healthcenter[i]);
    }
    for(int j=0; j<i; j++){
        int a,b,c;
        fscanf(fp,"%d %d %d",&a,&b,&c);
        a--;
        b--;
        //printf("%d %d %d\n",a+1,b+1,c);
        intersection[a][b]=c;
        intersection[b][a]=c;
    }
    for(int j=0; j<i; j++){
        for(int k=0; k<i; k++){
            //printf("%d ",intersection[j][k]);
        }
        //printf("\n");
    }

    int lowest_idx=1000;
    for(int loop=0; loop<f; loop++){
        if(bellman_ford(intersection,i,healthcenter[loop])<lowest_idx){
            lowest_idx=bellman_ford(intersection,i,healthcenter[loop]);
        }
    }

    printf("%d\n",lowest_idx);
    

    return 0;

}

