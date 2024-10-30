#!/usr/bin/python3

"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    LIFOCache defines:
    - implement custom put() and get()
    '''
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''
        add item to the cache using LIFO
        '''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_item = self.order.pop()
                print(f'DISCARD: {last_item}')
                del self.cache_data[last_item]
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        '''
        get an item by the key
        '''
        return self.cache_data.get(key, None)
