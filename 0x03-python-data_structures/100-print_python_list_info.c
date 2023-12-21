#include "Python.h"

/**
 * print_python_list_info - Print some basic info about Python lists.
 * @p: PyObject pointer.
 *
 * Your shared library will be compiled with this command line: gcc -Wall
 * -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so
 *  -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, list_size;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object;

	list_object = (PyListObject *)p;
	list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) list_size);
	printf("[*] Allocated = %d\n", (int)list_object->allocated);
	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) i, item_type);
	}
}
