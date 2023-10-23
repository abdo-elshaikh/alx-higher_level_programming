#include "Python.h"
#include <stdio.h>

/**
 * print_python_float - Print information about Python float objects
 * @p: Python object
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

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
 * print_python_list - Print information about Python list objects
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	int i = 0, list_len = 0;
	PyObject *item;

	printf("[*] Python list info\n");

	if (!PyList_Check(p) && !PyTuple_Check(p) && !PySet_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	list_len = PySequence_Size(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	for (; i < list_len; ++i)
	{
		item = PySequence_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);

		if (PyFloat_Check(item))
			print_python_float(item);

		Py_DECREF(item);
	}
}
