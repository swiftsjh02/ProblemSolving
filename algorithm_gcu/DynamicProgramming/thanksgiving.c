#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main(){

     FILE *fp = fopen("input.txt","r");

    if(fp==NULL){
        printf("no file\n");
        return -1;
    }

        
        
    while (1){
        int n;
        double sum=0;
        double student[1001];
        double avg=0;
        double ans1=0;
        double ans2=0;


        fscanf(fp,"%d",&n);
        if(n==0){
            break;
        }

        for(int i=0;i<n;i++){
            fscanf(fp,"%lf",&student[i]);
            sum+=student[i];
        }


        avg=round(sum/n/10)*10;
        

        for(int i=0; i<n; i++){
            if(student[i]>avg){
                ans1+=student[i]-avg;
            }
            else{
                ans2+=avg-student[i];
            }
        }

        if(ans1<ans2){
            printf("￦%.0lf\n",ans1);
            continue;
        }
        else{
            printf("￦%.0lf\n",ans2);
            continue;
        }
        
        
    }
}

