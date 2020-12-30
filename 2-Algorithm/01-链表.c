LNode  *create_LinkList(void)
/*  头插入法创建单链表,链表的头结点head作为返回值  */  
{    
	int data ;
	LNode *head, *p;
	head= (LNode*)malloc( sizeof(LNode));
	head->next = NULL;     /*  创建链表的表头结点head  */ 
	while (1){   
        scanf(“%d”, &data) ;
        if (data==32767)  
            break;
        p = (LNode*)malloc(sizeof(LNode));
        p–>data = data;     /*  数据域赋值  */
        p–>next = head–>next ;
        head–>next = p ; 
        /*  钩链，新创建的结点总是作为第一个结点  */
    }
	return (head);
}


LNode  *create_LinkList(void)
/*  尾插入法创建单链表,链表的头结点head作为返回值  */  
{   
	int data ;
	LNode *head, *p, *q;
	head=p=(LNode*)malloc(sizeof(LNode)); 
	p->next=NULL;        /*  创建单链表的表头结点head  */
	while (1){    
        scanf(“%d”,& data);
        if (data==32767)  
            break ;
        q = (LNode*)malloc(sizeof(LNode)); 
        q–>data = data;     /*   数据域赋值  */
        q–>next = p–>next;
        p–>next = q;
        p = q ; 
        /*钩链，新创建的结点总是作为最后一个结点*/
    }
	return (head);   
}