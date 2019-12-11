#include"lists.h"
/**
 *insert_node - insert node at idx
 *@number: n element of the structure
 *@head: header
 *Return: address of new element
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *new;
	unsigned int i = 0;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	aux = *head;
	while (number > aux->n)
	{
		aux = aux->next;
		i++;
		if (!aux)
			return (NULL);
	}
	new->n = number;
	new->next = aux->next;
	aux->next = new;
return (new);
}
