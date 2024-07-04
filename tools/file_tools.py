#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pathlib import Path

from common.log import logger
from common.public_methods import root_path


def exists_file(file_path: str, create: bool = False) -> str:
    """
    判断文件是否存在, 不存在则创建文件
    :param file_path: 文件路径
    :param create: 是否创建文件, 默认不创建
    :return: 返回文件路径
    """

    abs_path = root_path + file_path
    if not Path(abs_path).exists():
        logger.info(f"文件不存在: {abs_path}")
        if create:
            if Path(abs_path).is_dir():
                Path(abs_path).mkdir(parents=True, exist_ok=True)
            else:
                Path(abs_path).touch()
    return str(abs_path)


if __name__ == '__main__':
    print(exists_file('/conf/config.yaml'))
