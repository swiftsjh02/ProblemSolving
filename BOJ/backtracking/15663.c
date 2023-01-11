#include <stdio.h>
#include<stdlib.h>

int value=-1;

int static compare (const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}

void backtrack(int n,int m,int depth,int*arr,int*num,int idx){
    if(depth==m){
        for(int k=1; k<=m; k++){
            printf("%d ",arr[k]);
        }
        printf("\n");
        return;
    }
    int value=-1;
 

    for(int k=1; k<=n; k++){
        if(k!=idx){
            if(value!=num[k-1]){
                value=num[k-1];
                arr[depth+1]=num[k-1];
                backtrack(n,m,depth+1,arr,num,k);
            }  
         }
            
            
    }
    
    

}

int main(){
    int n,m=0;
    scanf("%d %d",&n,&m);
    int *num=malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        scanf("%d",&num[i]);
    }
    qsort(num,n,sizeof(int),compare);
    int *arr=malloc(sizeof(int)*(m+1));

    backtrack(n,m,0,arr,num,-1);

    return 0;
}