# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     srv_threaded
   Description :
   Author :       simplefly
   date：          2018/1/26
-------------------------------------------------
   Change Activity:
                   2018/1/26:
-------------------------------------------------
"""
__author__ = 'simplefly'
# Using multiple threads to serve several clients in parallel.

from simple_lib import zen_utils
from threading import Thread

def start_threads(listener, workers=4):
    t = (listener,)
    for i in range(workers):
        Thread(target=zen_utils.accept_connections_forever, args=t).start()

if __name__ == '__main__':
    listener = zen_utils.create_srv_socket(('', 1060))
    start_threads(listener)