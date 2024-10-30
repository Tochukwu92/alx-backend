#!/usr/bin/python3

"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
    LFUCache defines:
    - custom put() and get() using LFU replacement policy with LRU fallback
    '''
    def __init__(self):
        super().__init__()
        # Dictionary to track usage frequency of each key
        self.usage_frequency = {}

        # List to maintain order of keys for LRU
        self.usage_order = []

    def put(self, key, item):
        '''
        Add item to the cache using LFU replacement policy
        '''
        if key is None or item is None:
            return

        # Update existing key's frequency and position
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
            self.cache_data[key] = item
        else:
            # Check if cache is full
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                # Find LFU key(s) with LRU fallback if ties
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [
                    k for k in self.usage_order if self.usage_frequency[
                        k] == min_freq]
                lfu_key = lfu_keys[0]

                # Remove LFU (or LRU within ties) item from cache
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Insert the new item, set initial frequency to 1,
            # and add it to usage_order
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        '''
        Get an item by the key
        '''
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and order for LFU policy
        self.usage_frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
