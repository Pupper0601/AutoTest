#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from common._cache_ram import RamCache
from common._root_path import root_path
from common._read_config import conf_data


class DataInit:
    def __init__(self):
        self.ram = RamCache()
        self.ram.set("conf_path", root_path)
        self.ram.set("config", conf_data)
