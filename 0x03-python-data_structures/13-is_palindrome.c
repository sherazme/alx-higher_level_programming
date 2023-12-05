#include "lists.h"

/**
 * is_flag - Check if flag
 * @head: Head
 *
 * Return: 0 or 1
 */
int is_flag(listint_t **head)
{
	listint_t *list1, *list2, *head2;
	int flag = 1;

	/* Find the center of the list*/
	list2 = list1 = *head;
	while (list1 && list1->next)
	{
		list2 = list2->next;
		list1 = list1->next->next;
	}
	if (list1 == NULL)
		head2 = list2;
	else
		head2 = list2->next;

	/*Reverse the secned half of the list */
	list2 = NULL;
	while (head2 != NULL)
	{
		list1 = head2->next;
		head2->next = list2;
		list2 = head2;
		head2 = list1;
	}
	head2 = list2;

	/* Compar the first and secend part */
	list2 = *head;
	list1 = head2;
	while (list2 && list1)
	{
		if (list2->n != list1->n)
		{
			flag = 0;
			break;
		}
		list2 = list2->next;
		list1 = list1->next;
	}

	/* Rereverse the secend part and linke it to the first part */
	list2 = NULL;
	while (head2 != NULL)
	{
		list1 = head2->next;
		head2->next = list2;
		list2 = head2;
		head2 = list1;
	}
	head2 = list2;

	/* Return the result */
	if (flag)
		return (1);
	return (0);
}
