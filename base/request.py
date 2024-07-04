#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import json

import httpx

from common.log import logger
from common.public_methods import ram, fun_return_cache


class HttpRequest:
    def __init__(self):
        self.client = httpx.Client()

    def __request(self, method: str, url: str, **kwargs) -> httpx.Response:
        try:
            logger.info(self.__req_log(method, url, **kwargs))
            response = getattr(self.client, method.lower())(url, **kwargs)
            logger.info(self.__res_log(response))
            ram.set(url, response)
            return response
        except Exception as e:
            logger.error(f"请求程序错误: {e}")

    def get(self, url, **kwargs) -> httpx.Response:
        return self.__request('get', url, **kwargs)

    def post(self, url, **kwargs) -> httpx.Response:
        return self.__request('post', url, **kwargs)

    def put(self, url, **kwargs) -> httpx.Response:
        return self.__request('put', url, **kwargs)

    def delete(self, url, **kwargs) -> httpx.Response:
        return self.__request('delete', url, **kwargs)

    @staticmethod
    def __req_log(method: str, url: str, **kwargs) -> str:
        data_type = None
        data_value = None
        for key in ['params', 'data', 'json']:
            if kwargs.get(key) is not None:
                data_type = key
                data_value = kwargs.get(key)
                break
        return f"""
        请求数据:
          - method: {method},
          - url: {url},
          - headers: {kwargs.get('headers')},
          - {data_type}: {data_value},
        """

    @staticmethod
    def __res_log(response: httpx.Response) -> str:
        return f"""
        响应数据:
          - url: {response.url},
          - status_code: {response.status_code},
          - headers: {response.headers},
          - content: {response.content},
        """


if __name__ == '__main__':
    ur = "https://api.github.com"
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/json"
    }
    para = {
        "page": 1,
        "per_page": 10
    }
    HttpRequest().get(ur, headers=head, params=para)
    # HttpRequest().get(ur, headers=head, params=para)
    # print(ram.cache)
    # print(ram.get(ur).url)
    # print(ram.get(ur).status_code)
    # print(ram.get(ur).headers)
