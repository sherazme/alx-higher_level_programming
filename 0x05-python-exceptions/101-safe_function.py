#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    :param fct: Function pointer
    :param args: Function arguments
    :return: Returns function execution Or returns None and prints error
    """
    try:
        fun_exe = fct(*args)
        return (fun_exe)

    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)
