#!/usr/bin/python3
""" Module which has function that reads from a file """


def read_file(filename=""):
    """ Function which reads from a file

    Args:
        filename: filename

    Raises
        Exception: only if file can be opened
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
