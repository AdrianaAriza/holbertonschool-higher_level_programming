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

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	aux = *head;
	if (!*head)
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}
	while (number > aux->next->n)
	{
		aux = aux->next;
		i++;
		if (!aux->next)
		{
			aux->next = new;
			new->n = number;
			new->next = NULL;
			return (new);
		}
	}
	if (i == 0)
	{
		new->n = number;
		new->next = aux;
		*head = new;
		return (new);
	}
	new->n = number;
	new->next = aux->next;
	aux->next = new;
	return (new);
}
