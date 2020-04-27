#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Check if there is an infinite loop
 * @list: Linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;

	if (list == NULL || list->next == NULL)
		return (0);
	slow_p = list->next;
	fast_p = slow_p->next;

	while (slow_p != NULL && fast_p->next != NULL &&
		fast_p->next->next != NULL)
	{
		if (slow_p == fast_p)
			return (1);
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
	}

	return (0);
}
