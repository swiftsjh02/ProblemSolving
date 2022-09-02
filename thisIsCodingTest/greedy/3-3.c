#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int *mins;
    int n,m;
    int min_counter=0;
    scanf("%d %d",&n,&m);
    mins=malloc(sizeof(int)*m);
    for(int i=0; i<n; i++){
        char tmp[m];
        char s1[1000];
        int min=1000000;
        int z=0;
        scanf("%s\n",s1);

        char *ptr =strtok(s1," ");
        while(ptr!=NULL){
            tmp[z]=ptr;
            ptr=strtok(NULL," ");
            z++;
        }



        for(int j=0; j<m; j++){
            printf("%d\n",tmp[j]);
        }


        for(int j=0; j<m; j++){
            if(tmp[j]<min){
                min=tmp[j];
            }
        }

        

        mins[min_counter]=min;
        min_counter++;
        

    }



       
    int answer=0;
    for(int i=0; i<n; i++){
        
        if(mins[i]>answer){
            answer=mins[i];
            }

    }

    //printf("%d\n",answer);





    return 0;
}