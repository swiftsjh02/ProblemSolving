#include <stdio.h>
#include <stdlib.h>

int fibo(int* arr,int n,int len){
    if(arr[n]==-1){
        arr[n]=fibo(arr,n-1,len)+fibo(arr,n-2,len);
    }
    return arr[n];
}

int main(){
    int n;
    int *arr;
    scanf("%d",&n);
    arr=malloc(sizeof(int)*n+1);
    arr[0]=0;
    arr[1]=1;
    for(int i=2;i<n+1;i++){
        arr[i]=-1;
    }
    fibo(arr,n,n+1);
    printf("%d\n",arr[n]);

}