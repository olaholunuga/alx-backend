#!/usr/bin/env python3
""" BaseCaching module
"""
from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo cacheing now
    """

    def __init__(self):
        """init it all
        """
        super().__init__()
        self.queue = deque([])

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.queue:
                del_key = self.queue.popleft()
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an item by key
        """
        item = self.cache_data[key]
        if not key or not item:
            return None
        return item
