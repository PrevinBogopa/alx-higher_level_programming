#!/usr/bin/python3
"""The search and update module"""


def append_after(filename="", search_string="", new_string=""):
    """It nserts a line of text to a file after every line containing a specific string"""
    tmp = ""
    with open(filename) as f:
        for line in f:
            tmp += line
            if search_string in line:
                tmp += new_string
    with open(filename, "w") as w:
        w.write(tmp)
