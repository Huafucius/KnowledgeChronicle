//单向链表结构体
typedef struct Node {
	int data;
	struct Node* next;
}Node;

//增加：创建节点，并返回该节点的地址
Node* Create(int data) {
	Node* p = (Node*)malloc(sizeof(Node));
	if (p == NULL)
		return NULL;
	p->data = data;
	p->next = NULL;
	return p;
}

//删除：删除node节点的下一个节点
void Delete(Node* node) {
	Node* next_node = node->next;
	node->next = next_node->next;
	free(next_node);
}

//查找：找到key这个节点，并返回它上一个节点的地址（方便删除和插入）
Node* Search(Node* head, int key) {
	Node* p = head;
	while (p->next != NULL) {
		if (p->next->data == key)
			return p;
		else
			p = p->next;
	}
	return NULL;
}

//插入：把data插入到node节点的后面
void Insert(Node* node,int data) {
	Node* newnode = Create(data);
	newnode->next = node->next;
	node->next = newnode;
}

//打印：输入head节点，打印全部节点
void PrintAll(Node* head) {
	Node* p = head;
	while (p->next != NULL) {
		p = p->next;
		printf("%d\n", p->data);
	}
}
