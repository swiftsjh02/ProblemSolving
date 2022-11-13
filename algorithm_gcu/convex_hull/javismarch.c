
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct point
{
    double x;
    double y;
};

int crossProduct(struct point a, struct point b, struct point c) {    //finds the place of c from ab vector
   double d=(c.y-b.y)*(b.x-a.x)-(b.y-a.y)*(c.x-b.x);
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
double computedistance(struct point a,struct point b){
    double distance;
    distance=sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
    return distance;
}

double closestpairfrominitial(int *hull,struct point *points,int n,int count){
    double min=1000000000;
    struct point initial;
    initial.x=0;
    initial.y=0;
    for(int i=0; i<count; i++){
        if(min>computedistance(initial,points[hull[i]])){
            min=computedistance(initial,points[hull[i]]);
        }
    }
    
    return min;
}

void javismarch(struct point *points,int n){ 

    double silk;
    
    
    int c_index=findminx(points,n); //current index
    int *hull=(int *)malloc(sizeof(int)*n); //array stores index of points that on hull
    int count=0; //count of points on hull
    int next_index=0;
    while(1){
        hull[count]=c_index;
        for(int i=0; i<n; i++){
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
            if(cross==0){ //if 3 points are colinear, choose the one that is farthest from current point
                if(computedistance(points[c_index],points[i])>computedistance(points[c_index],points[next_index])){//
                    next_index=i;
                } //컨벡스헐을 만들때는 헐 위에 있는 점의 수를 최소화해야해서 일직선상에 점이 3개 놓이면 최대한 먼 점을 선택해야함.
            }
        }
        
        c_index=next_index;//update current index
        silk+=computedistance(points[c_index],points[hull[count]]); //add distance between current point and previous point
        if(hull[0]==c_index){ //if current point is same as first point, break
            break;

            }
        count++;
        }

        silk+=2*closestpairfrominitial(hull,points,n,count);
        printf("%.2lf",silk);
    
    

   
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
            fscanf(fp,"%lf %lf",&points[i].x,&points[i].y);
        }

        points[numofpoints+1].x=0;
        points[numofpoints+1].y=0;

        for(int i=0; i<numofpoints+1; i++){
            printf("%d:%lf %lf\n",i,points[i].x,points[i].y);
        }

        javismarch(points,numofpoints+1);

        numoftestcase--;
    }

    

    return 0;
}


