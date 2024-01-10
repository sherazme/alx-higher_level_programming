#!/usr/bin/python3
""" python to Jason """
import json


def to_json_string(my_obj):
    """ Convert python data to Json string

    Args:
      my_obj (object): Object to convert
    """
    return (json.dumps(my_obj))
