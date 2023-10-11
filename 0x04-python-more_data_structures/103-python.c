// Create two C functions that print some basic info about Python lists and Python bytes objects
// Return 0 if successful, 1 otherwise.
#include <python.h>
#include "/usr/include/python3.4/Python.h"
#include <stdio.h>
void print_python_list(PyObject *p)
{
    PyObject *obj;
    PyListObject *list_obj;
    int list_size, i = 0;
    /* print size of the list and allocations */
    list_size = PyList_Size(p);
    list_obj = (PyListObject *)p;

    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", (int)(list_obj->allocated));
    /* print elements of the list */
    while (i < list_size)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
        i++;
    }
}

void print_python_bytes(PyObject *p)
{
    PyObject *obj;
    PyBytesObject *bytes_obj;
    int list_size, i = 0;
    /* print size of the list and allocations */
    list_size = PyBytes_Size(p);
    bytes_obj = (PyBytesObject *)p;

    printf("[*] Size of the Python Bytes = %d\n", list_size);
    printf("[*] Allocated = %d\n", (int)(bytes_obj->allocated));
    /* print elements of the list */
    while (i < list_size)
    {
        obj = PyBytes_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
        i++;
    }
}