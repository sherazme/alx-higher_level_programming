#include "lists.h"

/**
 * check_cycle - Check for cycls
 * @list: Pointer to head
 * Return: 0 if there no cycle or 1 if there cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *list1, *list2;

	list1 = list2 = list;

	while (list1 && list2 && list2->next)
	{
		list1 = list1->next;
		list2 = list2->next->next;
		if (list1 == list2)
			return (1);
	}
	return (0);
}
