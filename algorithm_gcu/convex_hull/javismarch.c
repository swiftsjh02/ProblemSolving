#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct point
{
    int x;
    int y;
};

float computeangle(struct point a,struct point b){
    int dx,dy;
    float angle;
    dx=b.x-a.x;
    dy=b.y-a.y;
    if((dx>=0)&&(dy==0)){
        angle=0;
    }else{
        angle=abs(dy)/(abs(dx)+abs(dy));
        if((dx<0)&&(dy>=0)){
            angle=2-angle;
    }else if((dx<=0)&&(dy<0)){
        angle=2+angle;
    }else if((dx>0)&&(dy<0)){
        angle=4-angle;
    }
    }

    return angle*90.0;
}

int main(){
    printf("enter point a:");
    struct point a;
    scanf("%d %d",&a.x,&a.y);
    printf("enter point b:");
    struct point b;
    scanf("%d %d",&b.x,&b.y);
    printf("angle: %f\n",computeangle(a,b));
    return 0;
}