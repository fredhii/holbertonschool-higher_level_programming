#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list - Prints a python list.
 * @p: Python list.
 * Return: None.
 */
void print_python_list(PyObject *p)
{
	PyTypeObject *p_typ;
	PyObject *p_obj;
	unsigned long len;
	unsigned int i;

	if (PyList_Check(p))
	{
		len = ((PyVarObject *)p)->ob_size;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", len);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < len; i++)
		{
			p_obj = PySequence_GetItem(p, i);
			p_typ = p_obj->ob_p_typ;
			printf("Element %d: %s\n", i, p_typ->tp_name);
			if (strcmp(p_typ->tp_name, "bytes") == 0)
				print_python_bytes(p_obj);
		}
	}
}
/**
 * print_python_bytes - Prints python bytes.
 * @p: Python bytes.
 * Return: None.
 */
void print_python_bytes(PyObject *p)
{
	unsigned int i;
	unsigned long len;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = ((PyVarObject *)p)->ob_size;
	printf("  size: %lu\n", len);
	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);
	if (len >= 10)
		len = 10;
	else
		len++;
	printf("  first %lu bytes: ", len);
	for (i = 0; i < len; i++)
	{
		printf("%02x", str[i] & 0xff);
		if (i + 1 < len)
			printf(" ");
	}
	printf("\n");
}
