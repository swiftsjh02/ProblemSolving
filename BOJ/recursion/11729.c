#include <stdio.h>

int count=0;
int nums[50000][2];
int i=0;

void move(int n,int x,int y){

    if(n>1)
        move(n-1,x,6-x-y);
    nums[i][0]=x;
    nums[i][1]=y;
    i++;
    count++;

    if(n>1)
        move(n-1,6-x-y,y);
    


}

int main(){
    int n=0;
    scanf("%d",&n);
    move(n,1,3);
    printf("%d\n",count);
    for(int i=0; i<count; i++){
        printf("%d %d\n",nums[i][0],nums[i][1]);
    }


}