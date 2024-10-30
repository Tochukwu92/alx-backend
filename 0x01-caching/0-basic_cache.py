#!/usr/bin/python3

"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    BasicCache defines:
    - implement custom put() and get()
    '''
    def put(self, key, item):
        '''
        add item to the cache
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        get an item by the key
        '''
        return self.cache_data.get(key, None)
