#!/usr/bin/env python3
"""Fifo Cache Module Two"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class FIFOCache that inherits from BaseCaching and is a caching
        system: You must use self.cache_data - dictionary from the parent
        class BaseCaching You can overload def __init__(self): but don’t
        forget to call the parent init: super().__init__()
        def put(self, key, item):
    Args:
        Must assign to the dictionary self.cache_data the item value for th
        key. If key or item is None, this method should not do anything. If the
        number of items in self.cache_data is higher that BaseCaching.MAX_ITEM
    Return:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded and
        following by a new line def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
    """
    def __init__(self):
        """Initialize FIFOCache"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Add an item in the cache. If the key or item is None, do nothing."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.cache_order.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        """Get an item by key. If the key is None or doesn't exist,
            return None."""
        return self.cache_data.get[key, None]
