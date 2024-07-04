#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import cachetools

from common.log import logger
from base.decorator import singleton


@singleton
class RamCache:
    def __init__(self, maxsize=4096):
        self.cache = cachetools.LRUCache(maxsize)
        logger.info(f"RAM 缓存初始化成功, maxsize: {maxsize}")

    def set(self, key, value):
        self.cache[key] = value

    def get(self, key, default=None):
        return self.cache.get(key, default)

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def update(self, key, value):
        self.cache[key] = value

    def __contains__(self, key):
        return key in self.cache


def fun_return_cache(func):
    def wrapper(*args, **kwargs):
        ram_cache = RamCache()
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in ram_cache:
            res = func(*args, **kwargs)
            ram_cache.set(key, res)
            logger.info(f"缓存 {func.__name__} 函数的返回值: {res}")
            return res
        else:
            res = ram_cache.get(key)
            logger.info(f"读取 {func.__name__} 函数的缓存值: {res}")
            return res

    return wrapper


ram = RamCache()


if __name__ == '__main__':
    DataInit()
    ram = RamCache()
    print(ram.get("a"))


