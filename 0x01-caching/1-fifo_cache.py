#!/usr/bin/python3

"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFOCache defines:
    - implement custom put() and get()
    '''
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''
        add item to the cache
        '''
        if key is not None and item is not None:
            if key not in self.cache_data and len(
                    self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_item = self.order.pop(0)
                print(f'DISCARD: {first_item}')
                del self.cache_data[first_item]
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''
        get an item by the key
        '''
        return self.cache_data.get(key, None)
