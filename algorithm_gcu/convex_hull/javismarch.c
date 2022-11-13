#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct point
{
    float x;
    float y;
};

<<<<<<< HEAD

=======
int orientation(struct point p, struct point q, struct point r)
{
    int val = (q.y - p.y) * (r.x - q.x) -
              (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0; 	 // colinear
    return (val > 0)? 1: 2; 	// clock or counterclock wise
}
>>>>>>> 6fbe42931246614a9a84233d131af4cf1ef5edc2

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
   float d=(c.y-b.y)*(b.x-a.x)-(b.y-a.y)*(c.x-b.x);
   if(d>0){
    return 1; //ccw
   }
    else if(d<0){
     return -1; //cw
    }
    else{
     return 0; //collinear
    }
}

//function that finds the point with the smallest x coordinate
int findminx(struct point *points,int n){
    int minx=0;
    for(int i=1;i<n;i++){
        if(points[i].x<points[minx].x){
            minx=i;
        }
    }
    return minx;
}

void javismarch(struct point *points,int n){
    
<<<<<<< HEAD
    printf("%d\n",crossProduct(points[1],points[2],points[3]));
    int c_index=findminx(points,n);
    int *hull=(int *)malloc(sizeof(int)*n);
    int count=0;
    int next_index=0;
    while(1){
        hull[count]=c_index;
        for(int i=0; i<n-1; i++){
            if(i==c_index){
                continue;
            }
            if(next_index==c_index){
                next_index=i;
            }
            int cross=crossProduct(points[c_index],points[next_index],points[i]);
            if(cross==-1){
                next_index=i;
            }
            if(cross==0){
                if(computedistance(points[c_index],points[i])>computedistance(points[c_index],points[next_index])){
                    next_index=i;
                }
            }
        }
        count++;
        c_index=next_index;
        if(hull[0]==c_index){
            break;

            }
        }
    printf("%d\n",count);

=======
    int c_index=n-1; //current index
    int q=c_index%n;
    float silkused=2;
    printf("ccw: %d\n",orientation(points[c_index],points[3],points[0]));
    
>>>>>>> 6fbe42931246614a9a84233d131af4cf1ef5edc2
   
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