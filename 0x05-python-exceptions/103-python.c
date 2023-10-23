#include "Python.h"
#include <stdio.h>

/**
* print_python_float - print python float
* @p: python object
* Return: Nothing
*/
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AS_DOUBLE(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
/**
 * print_hexn - print hex
 * @str: string
 * @n: integer
 * Return: Nothing
 */
void print_hexn(const char *str, int n)
{
	int i = 0;

	for (; i < n - 1; ++i)
		printf("%02x ", (unsigned char)str[i]);

	printf("%02x", str[i]);
}
/**
* print_python_bytes - print python bytes
* @p: python object
* Return: Nothing
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *clone = (PyBytesObject *)p;
	int calc_bytes, clone_size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(clone))
	{
		clone_size = PyBytes_Size(p);
		calc_bytes = clone_size + 1;

		if (calc_bytes >= 10)
			calc_bytes = 10;

		printf("  size: %d\n", clone_size);
		printf("  trying string: %s\n", clone->ob_sval);
		printf("  first %d bytes: ", calc_bytes);
		print_hexn(clone->ob_sval, calc_bytes);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
/**
* print_python_list - print python list
* @p: python object
* Return: Nothing
*/
void print_python_list(PyObject *p)
{
	int i = 0, list_len = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *)p;

	printf("[*] Python list info\n");
	list_len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int)clone->allocated);

	for (; i < list_len; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
