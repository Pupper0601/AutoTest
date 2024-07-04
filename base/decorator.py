#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from functools import wraps


def singleton(cls):
    """
    装饰器，单例类的装饰器
    在装饰器里定义一个字典，用来存放类的实例, 如果实例字典中，存在类实例，直接取出返回类实例, 否则重新创建类实例;
    :param cls: 类的实例
    :return: 返回，装饰器中，被装饰的类函数
    """
    _instance = {}  # 在装饰器里定义一个字典，用来存放类的实例。

    @wraps(cls)
    def wrapper_class(*args, **kwargs):
        # 判断，类实例不在类实例的字典里，就重新创建类实例
        if cls not in _instance:
            # 将新创建的类实例，存入到实例字典中
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]   # 如果实例字典中，存在类实例，直接取出返回类实例
    return wrapper_class
