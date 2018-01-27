# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     in_zen2
   Description :
   Author :       simplefly
   date：          2018/1/26
-------------------------------------------------
   Change Activity:
                   2018/1/26:
-------------------------------------------------
"""
__author__ = 'simplefly'
# Multi-shot server for the use of inetd(8)

import socket, sys
from simple_lib import zen_utils

if __name__ == '__main__':
    listener = socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = sys.stderr = open('log.txt', 'a', buffering=1)
    listener.settimeout(8.0)
    try:
        zen_utils.accept_connections_forever(listener)
    except socket.timeout:
        print('Waited 8 seconds with no further connections; shutting down')