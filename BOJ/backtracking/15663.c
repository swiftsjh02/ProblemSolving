#include <stdio.h>
#include<stdlib.h>

int value=-1;
int check[10];

int static compare (const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}



void backtrack(int n,int m,int depth,int*arr,int*num){
    if(depth==m){
        for(int k=0; k<m; k++){
            printf("%d ",arr[k]);
        }
        printf("\n");
        return;
    }
    int value=-1;
 

    for(int k=0; k<n; k++){
        if(check[k]==0&&value!=num[k]){
            
                value=num[k];
                arr[depth]=num[k];
                check[k]=1;
                backtrack(n,m,depth+1,arr,num);
                check[k]=0;
            
         }
            
            
    }
    

}

int main(){
    int n,m=0;
    scanf("%d %d",&n,&m);
    int *num=(int *)malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        scanf("%d",&num[i]);
    }
    qsort(num,n,sizeof(int),compare);
    int *arr=(int *)malloc(sizeof(int)*(m+1));

    backtrack(n,m,0,arr,num);

    return 0;
}