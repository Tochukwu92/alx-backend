#!/usr/bin/python3

"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    MRUCache defines:
    - implement custom put() and get() using MRU caching strategy
    '''
    def __init__(self):
        super().__init__()
        self.order = []  # List to track the usage order for MRU

    def put(self, key, item):
        '''
        Add item to the cache using MRU replacement policy
        '''
        if key is not None and item is not None:

            # If key already exists, update its position in the order list
            if key in self.cache_data:
                self.order.remove(key)

            # If adding new item exceeds MAX_ITEMS,
            # discard the most recently used item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()  # Most recently used key
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            # Add the item to the cache and mark it as most recently used
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        '''
        Get an item by the key
        '''
        if key is None or key not in self.cache_data:
            return None

        # Update order list to mark this key as most recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
