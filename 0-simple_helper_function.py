#!/usr/bin/env python3
""" 0-simple_helper_function.py
"""


def index_range(page: int, page_size: int) -> tuple:
    """function returns a start index and an end index
    corresponding to the range of indexes to return in a
    list for those particular pagination parameters
    """
    res = (page_size * page) - page_size, page_size * page
    return res
