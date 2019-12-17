#include"lists.h"
/**
 *is_palindrome - is palindrome
 *@head: head
 *Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *end, *beg;
	int i = 0, j = 0;

	end = *head;
	beg = *head;

	if (!*head)
		return (1);
	while (end->next)
	{
		i++;
		end = end->next;
	}
	while (end->n == beg->n)
	{
		if (end == beg || j <= (i / 2))
			return (1);
		end--;
		beg++;
		j++;
	}
	return (0);
}
