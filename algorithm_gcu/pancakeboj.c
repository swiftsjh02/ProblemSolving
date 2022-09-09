#include <stdio.h>
#include <string.h>
#include <stdlib.h>


//make find max index function
int find_max_index(int *arr, int n){
    int max = arr[0];
    int max_index = 0;
    for(int i = 0; i < n; i++){
        if(arr[i] > max){
            max = arr[i];
            max_index = i;
        }
    }
    return max_index;
}



//make is sorted function
int is_sorted(int *arr, int n){
    for(int i = 0; i < n-1; i++){
        if(arr[i] > arr[i+1]){
            return 0;
        }
    }
    return 1;
}

void flip(int *arr, int n, int index){
    int *tmp=malloc(sizeof(int)*(index+1));
    
    int j=0;
    for(int i=index; i>=0; i--){
        tmp[j] = arr[i];
        j++;
    }

    for(int i=0; i<j; i++){
        
        arr[i]=tmp[i];
    }


    free(tmp);
}






int main(){
    
    FILE *fp = fopen("test.txt","r");

    if(fp==NULL){
        printf("no file\n");
        return -1;
    }
    char line[255];
    while(fgets(line,sizeof(line),fp)!=NULL){
        int cake[255];
        int answer[255];
        int idx_answer=0;
       
        printf("%s",line);
        
        
        int numofcake=0;
       
        char *ptr = strtok(line," ");
        while(ptr!=NULL){
            cake[numofcake]=atoi(ptr);
            ptr=strtok(NULL," ");
            numofcake++;
        }
        int len=numofcake;
     
        while(is_sorted(cake,numofcake)!=1){

            if(find_max_index(cake,numofcake)!=0){
                  answer[idx_answer]=find_max_index(cake,numofcake)+1;
                  flip(cake,numofcake,find_max_index(cake,numofcake));
                  
                  idx_answer++;
            }

           
            
            flip(cake,numofcake,numofcake-1);

            

            answer[idx_answer]=numofcake;
            idx_answer++;
            numofcake--;

            
            
        }


        if(idx_answer==0){
            printf("\n");
            printf("0\n");
        }
        else{
            printf("(");
            for(int i=0; i<len; i++){
                printf("%d ",cake[i]);
            }
            printf(")\n");
            for(int i = 0; i < idx_answer; i++){
                printf("%d ",answer[i]);
            }
            printf("0");
            printf("\n");
    
            }

        
      

    }

    fclose(fp);

}


