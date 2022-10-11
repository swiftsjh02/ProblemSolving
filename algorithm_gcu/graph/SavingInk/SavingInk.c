#include<stdio.h>
#include<stdlib.h>
#include<math.h>
double distance(double x1, double y1, double x2, double y2)
{
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2));
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

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            printf("%lf ",matrix[i][j]);
        }
        printf("\n");
    }


    return 0;
}