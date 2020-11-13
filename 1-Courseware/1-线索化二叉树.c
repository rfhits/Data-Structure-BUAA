typedef struct BiThrNode
{   
	ElemType  data;
	struct BiTreeNode *Lchild , *Rchild ; 
	int  Ltag , Rtag ;
}BiThrNode ;

// 先序线索化二叉树
void preorder_Threading(BiThrNode *T){  
	BiThrNode  *stack[MAX_NODE];
	BiThrNode  *last=NULL, *p ;
	int top=0 ;
	if  (T!=NULL){
	    stack[++top]=T;
	    while (top>0){  
		    p=stack[top--];
        	if (p->Lchild!=NULL)  
			    p->Ltag=0 ;
        	else {  
				p->Ltag=1 ;  
				p->Lchild=last ;  
			}
        	if(last!=NULL)
            	if (last->Rchild=NULL) last->Rtag=0 ;
            else{  
			    last->Rtag=1 ; 
		    	last->Rchild=p ; 
		    }
            last=p ;
            if (p->Rchild!=NULL) 
                stack[++top]=p->Rchild ; 
            if (p->Lchild!=NULL)
                    stack[++top]=p->Lchild ;
        }
        Last->Rtag=1;  /*   最后一个结点是叶子结点 */
    }
}

// 先序线索二叉树的先序遍历
void preorder_Thread_bt(BiThrNode *T){  
	BiThrNode  *p=T ;
	while (p!=NULL)
    {  
		visit(p->data) ;
        if (p->Ltag==0)  
            p=p->Lchild ;
        else  
            p=p->Rchild
    }
} 
