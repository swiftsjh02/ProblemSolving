#include <stdio.h>
#include <stdlib.h>

int n,m=0;

struct edge{
    int a;
    int b;
    int distance;
};

int static compare(const void* first,const void* second){
    if(((struct edge*)first)->distance>((struct edge*)second)->distance){
        return 1;
    }else if(((struct edge*)first)->distance<((struct edge*)second)->distance){
        return -1;
    }else{
        return 0;
    }
}

int getParent(int *parents,int a){
    if(parents[a]==a){
        return a;
    }
    parents[a]=getParent(parents,parents[a]);
    return parents[a];

}

int findParent(int *parents,int a,int b){
    a=getParent(parents,a);
    b=getParent(parents,b);
    if(a==b){
        return 1;
    }else{
        return 0;
    }
}

void unionFind(int *parents,int a,int b){
    a=getParent(parents,a);
    b=getParent(parents,b);
    if(a<b){
        parents[b]=a;
    }else{
        parents[a]=b;
    }

}



int main(){
    int a,b,c=0;
    int sum=0;
    scanf("%d",&n);
    scanf("%d",&m);
    int *parents=malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        parents[i]=i;
    }
    struct edge *edges=malloc(sizeof(struct edge)*m);
    for(int i=0; i<m; i++){
        scanf("%d %d %d",&a,&b,&c);
        edges[i].a=a-1;
        edges[i].b=b-1;
        edges[i].distance=c;
    }
    qsort(edges,m,sizeof(struct edge),compare);

    for(int i=0; i<m; i++){
        if(findParent(parents,edges[i].a,edges[i].b)==0){
            sum+=edges[i].distance;
            unionFind(parents,edges[i].a,edges[i].b);
            
        }
    }

    printf("%d\n",sum);
}