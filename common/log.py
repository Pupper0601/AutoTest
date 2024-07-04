#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import time
import loguru

from common._root_path import root_path
from functools import wraps


def singleton_class_decorator(cls):
    """ 装饰器，单例类的装饰器 """
    _instance = {}  # 在装饰器里定义一个字典，用来存放类的实例。

    @wraps(cls)
    def wrapper_class(*args, **kwargs):
        # 判断，类实例不在类实例的字典里，就重新创建类实例
        if cls not in _instance:
            # 将新创建的类实例，存入到实例字典中
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]   # 如果实例字典中，存在类实例，直接取出返回类实例

    return wrapper_class    # 返回，装饰器中，被装饰的类函数


@singleton_class_decorator
class Log:
    def __init__(self):
        """ 日志初始化 """
        self.logger_add()

    @staticmethod
    def get_log_path() -> str:
        """ 构建文件路径, 并验证文件是否存在 """
        lists: list = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).split(' ')

        return f"{root_path}/logs/{lists[0]}/{lists[1]}.log"

    def logger_add(self):
        loguru.logger.add(
            sink=self.get_log_path(),   # 水槽，分流器，可以用来输入路径
            rotation='00:00',   # 日志创建周期
            retention='1 day',  # 保存
            compression='zip',  # 文件的压缩格式
            encoding="utf-8",   # 编码格式
            enqueue=True,    # 具有使日志记录调用非阻塞的优点
            backtrace=True,  # 使日志记录包含有关异常的堆栈跟踪
            diagnose=True,   # 使日志记录包含有关异常地诊断信息
        )

    @property
    def get_logger(self):
        return loguru.logger


logger = Log().get_logger


if __name__ == '__main__':
    log = Log().get_logger
    log.info("测试日志")
    log.debug("测试日志")
    log.warning("测试日志")
    log.error("测试日志")
