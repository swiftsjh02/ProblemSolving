#include <stdlib.h>
#include <stdio.h>
#include <math.h>

struct ans{
    int a;
    int b;
    int x;
    int y;
    int d;
};

struct ans extended_euclid(struct ans x){
    if(x.b==0){
        x.d=x.a;
        x.x=1;
        x.y=0;
        return x;
    }
    int tmp=x.a;
    x.a=x.b;
    x.b=tmp%x.b;

    struct ans x2= extended_euclid(x);
    tmp=x2.x;
    x2.x=x2.y;
    x2.y=tmp-(x.a/x.b)*x2.y;
    printf("a:%d b:%d x:%d y:%d d:%d\n",x2.a,x2.b,x2.x,x2.y,x2.d);
    return x2;
}

int main(){
    int a,b=0;
    scanf("%d %d",&a,&b);
    struct ans x;
    x.a=a;
    x.b=b;
    struct ans ans1=extended_euclid(x);
    printf("%d %d %d\n",ans1.d,ans1.x,ans1.y);

}