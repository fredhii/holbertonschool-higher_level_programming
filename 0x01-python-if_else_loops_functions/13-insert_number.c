#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Insert a new node.
 * @head: Linked list
 * @number: Number to insert
 * Return: node address if Success, NULL if Fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new;

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	/* Check in first position */
	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	/* Check inside list */
	while (tmp->next)
	{
		if ((tmp->next)->n >= number)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	/* Insert in last position */
	tmp->next = new;
	new->next = NULL;
	return (new);
}
