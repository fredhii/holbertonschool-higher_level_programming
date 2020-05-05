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
	listint_t *current = *head, *temp;

	if (*head == NULL)
		return (NULL);
	while (current->next != NULL)
	{
		temp = current->next;
		current->next = temp->next;
		temp->next = *head;
		*head = temp;
	}
	return (*head);
}
/**
 * is_palindrome - Checks palidrom list.
 * @head: Single Linked list
 * Return: 0 if it's not a palindrome, 1 if it's a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *sta, *end;
	int len;

	if (*head == NULL)
		return (1);
	sta = *head;
	end = reverse_listint(&*head);

	for (len = 0; sta; len++)
		sta = sta->next;

	sta = *head;
	if (len % 2 == 0)
		len /= 2;
	else
	{
		len += 1;
		len /= 2;
	}
	while (len > 0 && sta && end)
	{
		if (sta->n != end->n)
			return (0);
		sta = sta->next;
		end = end->next;
	}
	return (1);
}
