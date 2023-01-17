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

int promising(int *arr,int depth){
    int flag=0;
    if(depth==0||depth==1){
        return flag;
    }
    if (arr[depth-1]<arr[depth-2]){
        flag=1;
        return flag;
    }
    return flag;
}



void backtrack(int n,int m,int depth,int*arr,int*num){
    if(depth==m&&promising(arr,depth)==0){
        for(int k=0; k<m; k++){
            printf("%d ",arr[k]);
        }
        printf("\n");
        return;
    }
    int value=-1;
 
    if(promising(arr,depth)==0){
        for(int k=0; k<n; k++){
            if(value!=num[k]){
                
                    value=num[k];
                    arr[depth]=num[k];
                    
                    backtrack(n,m,depth+1,arr,num);
                    
                
            }
                
                
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