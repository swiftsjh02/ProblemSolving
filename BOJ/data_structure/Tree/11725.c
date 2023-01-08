#include<stdio.h>
#include<stdlib.h>

struct node{
    int n;
    struct node *left;
    struct node *right;
};



struct node* insert(struct node* root,int data){
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
		if(root->left==NULL)
			root->left = insert(root->left,data);
		else if(root->right==NULL)
			root->right = insert(root->right,data);
        //printf("insert complete\n");
	}
	return root;
}

struct node* find_address(struct node* root, int number){
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

struct node* find_parent(struct node* root,struct node* prev,int number){
    struct node* post=root;
    if(root==NULL){
        //printf("no root\n");
        return NULL;
    }
    if(root->n==number){
        printf("%d\n",prev->n);
        return prev;
    }

    struct node* right=find_parent(root->right,post,number);
    struct node* left=find_parent(root->left,post,number);
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
   
    for(int i=0; i<n-1; i++){
        int a,b=0;
        scanf("%d %d",&a,&b);
        if(a==1){
            root->n=a;
            insert(root,b);
        }else{
            struct node* address = find_address(root,a);
            if(address==NULL){
                address=find_address(root,b);
                insert(address,a);
            }else{
            insert(address,b);
            }
        }
        
    }

 
    for(int i=2;i<=n; i++){
        find_parent(root,NULL,i);
    }
    

    

    return 0;
}