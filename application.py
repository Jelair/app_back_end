# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     application
   Description :
   Author :       simplefly
   date：          2018/1/25
-------------------------------------------------
   Change Activity:
                   2018/1/25:
-------------------------------------------------
"""
__author__ = 'simplefly'

import socket

def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)
    while True:
        sc, sockname = sock.accept()
