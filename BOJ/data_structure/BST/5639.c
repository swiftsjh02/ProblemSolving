#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *left;
    struct node *right;
}node;



node* insert(node* root,int data){
    if(root == NULL)
	{
		root = (node*)malloc(sizeof(node));
		root->right = root->left = NULL;
		root->data = data;
		return root;
	}
	else
	{
		if(data < root->data)
			root->left = insert(root->left,data);
		else
			root->right = insert(root->right,data);
	}
	return root;
}



//postorder
void postorderPrint(node* root)
{
	if(root==NULL)
		return;
    
    postorderPrint(root->left);
    postorderPrint(root->right);
    printf("%d\n",root->data);
    
	
}

int main(){
    int n =0;
    node* root=malloc(sizeof(struct node));
    int tmp=0;
    scanf("%d",&tmp);
    root->data=tmp;

    int k;
    while(scanf("%d",&k)!=EOF){
        insert(root,k);
    }

    postorderPrint(root);
}