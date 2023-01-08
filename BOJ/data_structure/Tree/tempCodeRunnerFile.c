#include<stdio.h>
#include<stdlib.h>

struct node{
    char n;
    struct node *left;
    struct node *right;
};



struct node* insert_left(struct node* root,char data){
    if(root == NULL)
	{   
        //printf("root is null\n");
		root = (struct node*)malloc(sizeof(struct node));
		root->right = root->left = NULL;
		root->n = data;
		return root;
	}
	else
	{
		if(root->left==NULL){
			root->left = insert_left(root->left,data);
        }
        //printf("insert complete\n");
	}
	return root;
}

struct node* insert_right(struct node* root,char data){
    if(root == NULL)
	{   
        //printf("root is null\n");
		root = (struct node*)malloc(sizeof(struct node));
		root->right = root->left = NULL;
		root->n = data;
		return root;
	}
	else
	{
		if(root->right==NULL){
			root->right = insert_right(root->right,data);
        }
        //printf("insert complete\n");
	}
	return root;
}

void preorderPrint(struct node* root)
{
	if(root==NULL)
		return;

    printf("%c",root->n);
    preorderPrint(root->left);
    preorderPrint(root->right);

    
	
}


void postorderPrint(struct node* root)
{
	if(root==NULL)
		return;

    postorderPrint(root->left);
    postorderPrint(root->right);
    printf("%c",root->n);


}

void inorderPrint(struct node* root)
{
	if(root==NULL)
		return;

    inorderPrint(root->left);
    printf("%c",root->n);
    inorderPrint(root->right);



}

struct node* find_address(struct node* root, char number){
    if(root==NULL){
        //printf("find address root is null\n");
        return NULL;
    }
    if(root->n==number){
       //printf("success\n");
        return root;
    }
    //printf("search left and right\n");
    struct node* left=find_address(root->left,number);
    struct node* right=find_address(root->right,number);
    if(left!=NULL){
        return left;
    }else{
        return right;
    }
}





int main(){
    int n=0;

    scanf("%d",&n);
    struct node *root=malloc(sizeof(struct node));
    root->left=NULL;
    root->right=NULL;
    char **temp=malloc(sizeof(char*)*30);
    for(int i=0; i<30; i++){
        temp[i]=malloc(sizeof(char)*3);
    }
    int tmpcnt=0;
   
    for(int i=0; i<n; i++){
        char a,b,c;
        scanf(" %c %c %c",&a,&b,&c);

 
        if(a=='A'){
            root->n=a;
            insert_left(root,b);
            insert_right(root,c);
        }else{
            struct node* address = find_address(root,a);
            if(address!=NULL){
                if(b!='.'){
                    insert_left(address,b);
                }else{
                    
                }
                if(c!='.'){
                    insert_right(address,c);
                }else{

                }
            }else{
                temp[tmpcnt][0]=a;
                temp[tmpcnt][1]=b;
                temp[tmpcnt][2]=c;
                tmpcnt+=1;
            }
        }
        
    }

    for(int i=0; i<tmpcnt; i++){
        struct node* address=find_address(root,temp[i][0]);
        if(address!=NULL){
                if(temp[i][1]!='.'){
                    insert_left(address,temp[i][1]);
                }else{
                    
                }
                if(temp[i][2]!='.'){
                    insert_right(address,temp[i][2]);
                }else{

                }
            }
    }

    preorderPrint(root);
    printf("\n");
    inorderPrint(root);
    printf("\n");
    postorderPrint(root);
    printf("\n");


    return 0;
}