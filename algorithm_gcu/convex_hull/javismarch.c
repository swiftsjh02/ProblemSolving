#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct point
{
    float x;
    float y;
};

int orientation(struct point p, struct point q, struct point r)
{
    int val = (q.y - p.y) * (r.x - q.x) -
              (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0; 	 // colinear
    return (val > 0)? 1: 2; 	// clock or counterclock wise
}

float computeangle(struct point a,struct point b){
    if(a.x==b.x&&a.y==b.y){
        return 370;
    }
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


float computedistance(struct point a,struct point b){
    float distance;
    distance=sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
    return distance;
}

int crossProduct(struct point a, struct point b, struct point c) {    //finds the place of c from ab vector
   int y1 = a.y - b.y;
   int y2 = a.y - c.y;
   int x1 = a.x - b.x;
   int x2 = a.x - c.x;
   return y2*x1 - y1*x2; //if result < 0, c in the left, > 0, c in the right, = 0, a,b,c are collinear
}

void javismarch(struct point *points,int n){
    
    int c_index=n-1; //current index
    int q=c_index%n;
    float silkused=2;
    printf("ccw: %d\n",orientation(points[c_index],points[3],points[0]));
    
   
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
    
    printf("number of case: %d\n",numoftestcase);
    while (numoftestcase>0)
    {
        int numofpoints;
        fscanf(fp,"%d",&numofpoints);
        printf("number of points: %d\n",numofpoints);
        struct point *points=(struct point*)malloc(sizeof(struct point)*numofpoints+1);
        
        for(int i=0; i<numofpoints; i++){
            fscanf(fp,"%f %f",&points[i].x,&points[i].y);
        }

        points[numofpoints+1].x=0;
        points[numofpoints+1].y=0;

        for(int i=0; i<numofpoints+1; i++){
            printf("%d:%f %f\n",i,points[i].x,points[i].y);
        }

        javismarch(points,numofpoints+1);

        numoftestcase--;
    }

    

    return 0;
}