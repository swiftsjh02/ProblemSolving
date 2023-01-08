#include <stdio.h>
#include <stdlib.h>

int cnt=0;

int promising(int i,int *arr){
    int k=1;
    int flag=1;
    while(k<i && flag){
        if(arr[i]==arr[k] || abs(arr[i]-arr[k])==i-k)
            flag=0;
        k++;
    }
    return flag;
}

void n_queen(int i,int n,int *arr){
    if(i==n){
        cnt+=1;
    }
    if(promising(i,arr)==1){
        for(int j=1; j<=n; j++){
            arr[i+1]=j;
            n_queen(i+1,n,arr);
        }
    }
}

int main(){
    int n=0;
    scanf("%d", &n);
    int *arr = (int*)malloc(sizeof(int)*n+1);
    n_queen(0,n,arr);
    printf("%d", cnt);
    return 0;
}