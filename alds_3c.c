#include <stdio.h>
#include <malloc.h>
#include <string.h>

#define DEL_1ST  "deleteFirst"
#define DEL_LAST "deleteLast"
#define DELETE "delete"
#define INSERT "insert"

struct _node{
	struct _node *prev ;
	struct _node *next ;
	int val ;
} ;

void print_list(struct _node *top) {
	struct _node *node ;
	for (node = top; node; node = node->next) {
		printf("%d ", node->val) ;
	}
	printf("\n") ;
}

void free_top(struct _node **top, struct _node **bot) {
	struct _node *free_node = *top ;
	*top = (*top)->next ;
	if (!*top) *bot = NULL ;
	else (*top)->prev = NULL ;
	free (free_node) ;
	//print_list(*top) ;
}

void free_bot(struct _node **top, struct _node **bot) {
	struct _node *free_node = *bot ;
	*bot = (*bot)->prev ;
	if (!*bot) *top = NULL ;
	else (*bot)->next = NULL ;
	free (free_node) ;
	//print_list(*top) ;
}

void insert_node(int val, struct _node **top, struct _node **bot) {
	struct _node *node ;

	node = malloc(sizeof(struct _node)) ;
	if (*top) (*top)->prev = node ;
	node->val = val ;
	node->next = *top ;
	node->prev = NULL ;
	*top = node ;
	if (!*bot) *bot = node ;
	//print_list(*top) ;
}

void free_mid(struct _node *node) {
	node->next->prev = node->prev ;
	node->prev->next = node->next ;
	free(node) ;
}

void free_node(int val, struct _node **top, struct _node **bot) {
	struct _node *node ;
	for (node = *top; node; node = node->next) {
		if (node->val == val) {
			if (node == *top) free_top(top, bot) ; 
			else if (node == *bot) free_bot(top, bot) ; 
			else free_mid(node) ;
			return ;
		}
	}
}

int main(void) {
	int i ;
	struct _node *node ;
	struct _node *top =  NULL ;
	struct _node *bot = NULL ;
	char buf[100] ;
	int n ;

	fscanf(stdin, "%d\n", &n) ;
	for (i=0; i<n; i++) {
		fgets(buf, sizeof(buf), stdin) ;
		//printf("%s", buf) ;

		if (!strncmp(buf, DEL_1ST, sizeof(DEL_1ST)-1)) {
			//printf("delFirst %d\n", top->val) ;
			free_top(&top, &bot) ;
		}
		else if (!strncmp(buf, DEL_LAST, sizeof(DEL_LAST)-1)) {
			//printf("delLast %d\n", bot->val) ;
			free_bot(&top, &bot) ;
		}
		else {
			char cmd[100] ;
			int val ;

			sscanf(buf, "%s %d", cmd, &val) ;
			if (!strncmp(cmd, INSERT, sizeof(INSERT))) {
				insert_node(val, &top, &bot) ;
			}
			else if (!strncmp(cmd, DELETE, sizeof(DELETE))) {
				free_node(val, &top, &bot) ;
			}
			else printf("Unexpected input %s\n", buf) ;
		}
	}

	for (node = top; node; node = node->next) {
		if (node != bot) printf("%d ", node->val) ;
		else printf("%d\n", node->val) ;
	}
}
