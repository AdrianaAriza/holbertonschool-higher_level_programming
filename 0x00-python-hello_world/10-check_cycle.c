#include"lists.h"
#include<stdlib.h>
/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *@list: list to check
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t **arr, *aux;
	int cont = 1, i = 0, j = 0, flag = 0, k = 0;

	if (list)
		arr = malloc(sizeof(listint_t) * 1);
	aux = list;
	arr[i] = aux;
	while (aux->next)
	{
		cont++, i++;
		j = 0;
		while (arr[j])
		{
			if (arr[j] == aux->next)
			{
				k = 0;
				while (arr[k])
					free(arr[k]), k++;
				free(arr);
				return (1);
			}
			j++;
		}
		arr = _realloc(arr, (cont - 1), cont);
		arr[i] = aux->next;
		aux = aux->next;
	}
	return (flag);
}

/**
 *_realloc - realloc
 *@ptr: old pointer
 *@old_size: old_size
 *@new_size: new_size
 *Return: new puntero
 */
listint_t **_realloc(listint_t **ptr, unsigned int old_size,
		     unsigned int new_size)
{
	listint_t **newp;
	unsigned int i = 0;

	newp = malloc(sizeof(listint_t) * new_size);
	if (newp == NULL)
		return (NULL);
	if (ptr != NULL)
	{
		for (i = 0; i < old_size && i < new_size; i++)
			newp[i] = ptr[i];
	}
	i = 0;
	return (newp);
}
