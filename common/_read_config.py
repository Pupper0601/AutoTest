#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import yaml

from common.log import logger
from common._root_path import root_path


def read_config(conf_path: str) -> dict:
    with open(conf_path, "r", encoding="utf-8") as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
        logger.info(f"读取配置文件成功: {conf_path}")
    return config


conf_data = read_config(root_path+'/conf/config.yaml')
