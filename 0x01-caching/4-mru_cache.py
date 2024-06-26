#!/usr/bin/env python3
"""MRU Module Four"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class MRUCache that inherits from BaseCaching and is a caching system:
        You must use self.cache_data - dictionary from the parent class
        BaseCaching You can overload def __init__(self): but don’t forget to
        call the parent init: super().__init__() def put(self, key, item)
    Args:
        Must assign to the dictionary self.cache_data the item value
        for the key key. If key or item is None, this method should
        not do anything. If the number of items in self.cache_data is
        higher that BaseCaching.MAX_ITEMS: you must discard the most
        recently used item (MRU algorithm) you must print DISCARD:
        with the key discarded and following by a new line def get(self, key)
    Return:
        return the value in self.cache_data linked to key. If key is
        None or if the key doesn’t exist in self.cache_data, return None
    """
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """Put an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.mru.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recently_used = self.mru.pop()
            del self.cache_data[most_recently_used]
            print("DISCARD: {}".format(most_recently_used))

        self.cache_data[key] = item
        self.mru.append(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.mru.remove(key)
        self.mru.append(key)
        return self.cache_data[key]
