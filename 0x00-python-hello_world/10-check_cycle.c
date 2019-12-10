#include"lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *@list: list to check
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *aux2, *aux;

	if (!list)
		return (0);
	aux = list;
	aux2 = list;
	while (aux && aux->next && aux2->next->next)
	{
		aux = aux->next;
		aux2 = aux2->next->next;
		if (aux == aux2)
			return (1);
	}
	return (0);
}
