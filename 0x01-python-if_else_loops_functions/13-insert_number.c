#include "lists.h"

/**
 * insert_node - Insert number
 * @head: Head
 * number: number to insert
 *
 * Return: address or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *current;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	current = *head;
	while (current->next && current->next->n < number)
		current = current->next;

	node->next = current->next;
	current->next = node;

	return (node);
}
