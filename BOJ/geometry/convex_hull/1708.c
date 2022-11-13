#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct point
{
    float x;
    float y;
};




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

//function that computes distance between two points
float computedistance(struct point a,struct point b){
    float distance;
    distance=sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
    return distance;
}

void javismarch(struct point *points,int n){
    
    
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

   
}




int main(){
    int n;
    scanf("%d",&n);
    struct point *points=(struct point *)malloc(sizeof(struct point)*n);
    for(int i=0;i<n;i++){
        scanf("%f %f",&points[i].x,&points[i].y);
    }
    javismarch(points,n);
    return 0;
}