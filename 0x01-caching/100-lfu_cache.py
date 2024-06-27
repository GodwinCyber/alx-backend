#!/usr/bin/env python3
"""LFU cache Module Five"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """A class LFUCache that inherits from BaseCaching and is a caching system:
        You must use self.cache_data - dictionary from the parent class
        BaseCaching You can overload def __init__(self): but don’t forget
        to call the parent init: super().__init__()def put(self, key, item):
    Args:
        Must assign to the dictionary self.cache_data the item value for
        the key key. If key or item is None, this method should not do
        anything. If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS: you must discard the least frequency used
        item (LFU algorithm) if you find more than 1 item to discard, you
        must use the LRU algorithm to discard only the least recently used
        you must print DISCARD: with the key discarded and following by a
        new line def get(self, key):
    Return:
        return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
    """
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.freq = defaultdict(int)
        self.usage_order = {}
        self.min_freq = 0
        self.lru = defaultdict(list)

    def put(self, key, item):
        """Put an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.get(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq_keys = self.lru[self.min_freq]
                if min_freq_keys:
                    lru_key = min_freq_keys.pop(0)
                    if not min_freq_keys:
                        del self.lru[self.min_freq]
                    del self.cache_data[lru_key]
                    del self.freq[lru_key]
                    del self.usage_order[lru_key]
                    print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.freq[key] = 1
            self.lru[1].append(key)
            self.min_freq = 1

        self.usage_order[key] = self.usage_order.get(key, 0) + 1

    def get(self, key):
        """Get an item by key. If the key is None or does not exist,
            return None"""
        if key is None or key not in self.cache_data:
            return None

        freq = self.freq[key]
        self.lru[freq].remove(key)
        if not self.lru[freq]:
            del self.lru[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.freq[key] += 1
        new_freq = self.freq[key]
        if new_freq not in self.lru:
            self.lru[new_freq] = []
        self.lru[new_freq].append(key)
        self.usage_order[key] = self.usage_order.get(key, 0) + 1

        return self.cache_data[key]
