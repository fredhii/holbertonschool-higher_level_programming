#include <Python.h>

/**
 * print_python_list_info - Prints basic info from python list.
 * @p: Python list.
 * Return: None.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t len, alloc, i;
	PyObject *p_obj;

	len = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < len; i++)
	{
		p_obj = PyList_GetItem(p, i);
		printf("Element %ls: %s\n", i, Py_TYPE(p_obj)->tp_name)
	}
}
