#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome.
 * @head: Head of the list.
 *
 * Return: 0 if it is not palindrome, 1 if it is palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *head2;
	int palindrome = 1;

	/* Find the center of the list*/
	slow = fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast == NULL)
		head2 = slow;
	else
		head2 = slow->next;

	/*Reverse the secned half of the list */
	slow = NULL;
	while (head2 != NULL)
	{
		fast = head2->next;
		head2->next = slow;
		slow = head2;
		head2 = fast;
	}
	head2 = slow;

	/* Compar the first and secend part */
	slow = *head;
	fast = head2;
	while (slow && fast)
	{
		if (slow->n != fast->n)
		{
			palindrome = 0;
			break;
		}
		slow = slow->next;
		fast = fast->next;
	}

	/* Rereverse the secend part and linke it to the first part */
	slow = NULL;
	while (head2 != NULL)
	{
		fast = head2->next;
		head2->next = slow;
		slow = head2;
		head2 = fast;
	}
	head2 = slow;

	/* Return the result */
	if (palindrome)
		return (1);
	return (0);
}
