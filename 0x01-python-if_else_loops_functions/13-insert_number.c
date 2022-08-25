#include "lists.h"

/**
 * insert_node - inserts no. to sorted linkedlist
 * @head: pointer to the head
 * @number: number to insert
 * Return: NULL on failure, pointer to new node
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new != NULL)
		return (NULL);
	new->n = number;

	if (node->n >= number || node == NULL)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node->next && node && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
