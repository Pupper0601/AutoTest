#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from pprint import pprint

import yaml

from tools.file_tools import exists_file
from common.public_methods import fun_return_cache
from common.log import logger


@fun_return_cache
def read_yaml(file_path: str) -> dict:
    try:
        yaml_path = exists_file(file_path)
        if yaml_path:
            f = open(yaml_path, 'r', encoding='utf-8')
            return yaml.load(f, Loader=yaml.FullLoader)
    except Exception as e:
        logger.error(f"读取 yaml 文件错误: {e}")


if __name__ == '__main__':
    # conf = read_yaml('/conf/config.yaml')
    # print(conf)
    # print(ram.cache)
    pprint(read_yaml('/conf/config.yaml'))
    # print(read_yaml('/conf/config.yaml'))
