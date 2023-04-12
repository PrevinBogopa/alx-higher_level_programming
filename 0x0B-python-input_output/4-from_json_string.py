#!/usr/bin/python3
""" Module Which has  a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON representation

    Args:
        my_str: JSON representation

    Raises:
        Exception: when the string cannot be decoded

    """
    return json.loads(my_str)