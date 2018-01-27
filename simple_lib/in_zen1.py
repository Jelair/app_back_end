# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     in_zen1
   Description :
   Author :       simplefly
   date：          2018/1/26
-------------------------------------------------
   Change Activity:
                   2018/1/26:
-------------------------------------------------
"""
__author__ = 'simplefly'
# Single-shot server for the use of inetd(8)

import socket, sys
from simple_lib import zen_utils

if __name__ == '__main__':
    sock = socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = sys.stderr = open('log.txt', 'a', buffering=1)
    address = sock.getpeername()
    print('Accepted connection from {}'.format(address))
    zen_utils.handle_conversation(sock, address)