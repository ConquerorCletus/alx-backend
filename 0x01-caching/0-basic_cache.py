"""
This module contains class BasicCache which inherits.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key or item is None:
            pass

        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        gets the item at a given key.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
