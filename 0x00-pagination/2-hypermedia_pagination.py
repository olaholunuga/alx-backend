#!/usr/bin/env python3
""" 0-simple_helper_function.py
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """function returns a start index and an end index
    corresponding to the range of indexes to return in a
    list for those particular pagination parameters
    """
    res = (page_size * page) - page_size, page_size * page
    return res


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method to get paginations
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        startindex, endindex = index_range(page, page_size)

        try:
            res = self.dataset()
            return res[startindex: endindex]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        method to get hyper
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        hyper_dict = {}
        hyper_dict["page_size"] = len(data)
        hyper_dict["page"] = page
        hyper_dict["data"] = data
        hyper_dict["next_page"] = page + 1 if total_pages >= page + 1 else None
        hyper_dict["prev_page"] = page - 1 if page > 1 else None
        hyper_dict["total_pages"] = total_pages

        return hyper_dict
