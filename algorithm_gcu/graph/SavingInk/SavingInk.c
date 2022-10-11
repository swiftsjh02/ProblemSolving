#include<stdio.h>
#include<stdlib.h>
#include<math.h>
double distance(double x1, double y1, double x2, double y2)
{
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2));
}

double prim(double matrix[][100],int n,int*node){
    int start=0;
    int *visited=(int*)malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        visited[i]=0;
    }
    visited[0]=1;
    double distance=0;

    for(int i=0; i<n-1; i++){
        double min=100000000;
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
    FILE *fp=fopen("input.txt","r");
    if(fp==NULL){
        printf("File not found");
        return 0;
    }

    int n;
    fscanf(fp,"%d",&n);
    double input[100][2];
    double matrix[100][100];
    int *node=(int *)malloc(n*sizeof(int));
    for(int i=0; i<n; i++){
        fscanf(fp,"%lf %lf",&input[i][0],&input[i][1]);
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            matrix[i][j]=distance(input[i][0],input[i][1],input[j][0],input[j][1]);
        }
    }

    printf("%0.2lf\n",prim(matrix,n,node));


    return 0;
}