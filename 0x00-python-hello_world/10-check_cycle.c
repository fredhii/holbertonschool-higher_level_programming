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
	int nodes = 1;

	if (list == NULL || list->next == NULL)
		return (0);
	slow_p = list->next;
	fast_p = (list->next)->next;
	while (fast_p)
	{
		if (slow_p == fast_p)
		{
			slow_p = list;
			for (; slow_p != fast_p; nodes++)
			{
				slow_p = slow_p->next;
				fast_p = fast_p->next;
			}
			slow_p = slow_p->next;
			for (; slow_p != fast_p; nodes++)
				slow_p = slow_p->next;
			return (1);
		}
		slow_p = slow_p->next;
		fast_p = (fast_p->next)->next;
	}

	return (0);
}
