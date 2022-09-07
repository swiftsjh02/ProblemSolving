#include <stdio.h>
#include<stdlib.h>

void flip(int *arr, int n, int index){
    int *tmp=malloc(sizeof(int)*(index+1));
    
    int j=0;
    for(int i=index; i>=0; i--){
        tmp[j] = arr[i];
        j++;
    }



    for(int i=0; i<j; i++){
        printf("%d ", tmp[i]);
        arr[i]=tmp[i];
    }

    

    free(tmp);


}


int main(){
    int arr[5] = {4,3,2,5,1};
    flip(arr, 5, 3);
    
    for(int i=0; i<5; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}