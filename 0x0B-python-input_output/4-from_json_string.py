#!/usr/bin/python3
""" Pars Json data """
import json


def from_json_string(my_str):
    """ Pars data from json

    Args:
      my_str (str): String contains data
    """
    return (json.loads(my_str))
