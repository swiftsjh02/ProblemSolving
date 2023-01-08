#include <stdio.h>
#include<stdlib.h>

int promising(int *arr,int depth){
    int flag=0;
    if(depth==0||depth==1){
        return flag;
    }
    if (arr[depth]<arr[depth-1]){
        flag=1;
        return flag;
    }
    return flag;
}

void backtrack(int n,int m,int depth,int*arr){
    if(depth==m&&promising(arr,depth)==0){
        for(int k=1; k<=m; k++){
            printf("%d ",arr[k]);
        }
        printf("\n");
        return;
    }
    
    if(promising(arr,depth)==0){
        for(int k=1; k<=n; k++){
            arr[depth+1]=k;
            backtrack(n,m,depth+1,arr);
        }
    }
    

}

int main(){
    int n,m=0;
    scanf("%d %d",&n,&m);
    int *arr=malloc(sizeof(int)*(m+1));

    backtrack(n,m,0,arr);

    return 0;
}