#!/usr/bin/python3
""" Json representation """
import json


def save_to_json_file(my_obj, filename):
    """ Write object to text file using json representation

    Args:
      my_obj: Object
      filename: Name of file where to store data
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
