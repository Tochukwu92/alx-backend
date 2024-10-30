#!/usr/bin/python3

"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    LRUCache defines:
    - implement custom put() and get() using LRU caching strategy
    '''
    def __init__(self):
        super().__init__()
        self.order = []  # List to track the usage order for LRU

    def put(self, key, item):
        '''
        Add item to the cache using LRU replacement policy
        '''
        if key is not None and item is not None:
            # If key is already in cache, remove it to update its position
            if key in self.cache_data:
                self.order.remove(key)
            # If adding new item exceeds MAX_ITEMS,
            # remove the least recently used item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)  # Least recently used key
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the item to the cache and update its usage order
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        '''
        Get an item by the key
        '''
        if key is None or key not in self.cache_data:
            return None

        # Update order list to mark this key as recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
