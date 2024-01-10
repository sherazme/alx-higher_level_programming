#!/usr/bin/python3
""" Deserialize json file """
import json


def load_from_json_file(filename):
    """ Pars a json data

    Args:
      filename: File name to retrive data from
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return (json.load(f))
