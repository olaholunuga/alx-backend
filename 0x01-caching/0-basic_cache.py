#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherets from the BasicCaching Class
    """

    def __init__(self):
        """using super for init
        """
        super().__init__()

    def put(self, key, item):
        """caching items
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get cached items
        """
        item = self.cache_data.get(key)
        if not key:
            return None
        return item
