#!/usr/bin/env python3
""" BaseCaching module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
                "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
                "get must be implemented in your cache class")


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
