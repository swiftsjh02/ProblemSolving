#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct point
{
    float x;
    float y;
};

float computeangle(struct point a,struct point b){
    int dx,dy;
    float angle;
    dx=b.x-a.x;
    dy=b.y-a.y;
    if((dx>=0)&&(dy==0)){
        angle=0;
    }else{
        angle=(float)abs(dy)/(abs(dx)+abs(dy));
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
    FILE *fp=fopen("input.txt","r");
    if(fp==NULL){
        printf("Error in opening file");
        exit(0);
    }
    int numoftestcase;
    char t[10];
    fscanf(fp,"%d",&numoftestcase);
    fscanf(fp,"%s",t);
    printf("number of case: %d\n",numoftestcase);
    while (numoftestcase>0)
    {
        int numofpoints;
        fscanf(fp,"%d",&numofpoints);
        printf("number of points: %d\n",numofpoints);
        struct point *points=(struct point*)malloc(sizeof(struct point)*numofpoints);
        
        for(int i=0; i<numofpoints; i++){
            fscanf(fp,"%f %f",&points[i].x,&points[i].y);
        }

        for(int i=0; i<numofpoints; i++){
            printf("%f %f\n",points[i].x,points[i].y);
        }

        numoftestcase--;
    }
    

    return 0;
}