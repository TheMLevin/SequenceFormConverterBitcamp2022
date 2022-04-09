import functools
from typing import Callable


def cache(func: Callable):
    @functools.wraps(func)
    def cache_wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache_wrapper.cache:
            cache_wrapper.cache[key] = func(*args, **kwargs)
        return cache_wrapper.cache[key]
    cache_wrapper.cache = dict()
    return cache_wrapper
