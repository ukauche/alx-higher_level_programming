#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint - Singly linked list.
 * @x: integer.
 * @next: Pointer to the next node.
 *
 * Description: Singly linked list node structure
 */
typedef struct listint
{
	int x;
	struct listint *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int x);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
