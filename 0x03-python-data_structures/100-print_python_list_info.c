#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - Prints basic info from python list.
 * @p: Python list.
 * Return: None.
 */
void print_python_list_info(PyObject *p)
{
	int len, alloc, i;
	PyObject *p_obj;

	len = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < len; i++)
	{
		printf("Element %d: ", i);
		p_obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(p_obj)->tp_name);
	}
}
