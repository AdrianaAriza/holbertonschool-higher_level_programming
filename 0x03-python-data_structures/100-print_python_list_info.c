#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 *print_python_list_info - print list info
 *@p: object
 *Return: void
 */
void print_python_list_info(PyObject *p)
{
	int l, a, i;
	PyObject *aux;
	a = ((PyListObject *)p)->allocated;
	l =  Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", l);
	printf("[*] Allocated = %d\n", a);

	for (i = 0; i < l; i++)
	{
		printf("Element %d: ", i);
		aux = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(aux)->tp_name);
	}
}
