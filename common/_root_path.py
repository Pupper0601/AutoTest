#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pathlib import Path


def get_root_path() -> str:
    """ 获取当前项目的根路径 """
    return str(Path.cwd().parent).split('AutoTest')[0] + 'AutoTest'


root_path = get_root_path()


if __name__ == '__main__':

    print(get_root_path())
