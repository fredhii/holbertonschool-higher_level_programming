#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_listint - Reverse a linked list.
 * @head: Linked list.
 * Return: Inverse linked list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *next, *prev = NULL;

	if (*head == NULL)
		return (NULL);
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - Checks palidrom list.
 * @head: Single Linked list
 * Return: 0 if it's not a palindrome, 1 if it's a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux, *tmp, *rev;
	int len, i;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	aux = *head;
	for (len = 0; aux; len++)
		aux = aux->next;

	tmp = *head;
	for (i = 0; i < (len / 2) - 1; i++)
		tmp = tmp->next;

	if (len % 2 == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	aux = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&aux);

	return (1);
}
