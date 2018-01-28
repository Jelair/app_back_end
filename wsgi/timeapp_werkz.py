# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     timeapp_werkz
   Description :
   Author :       simplefly
   date：          2018/1/28
-------------------------------------------------
   Change Activity:
                   2018/1/28:
-------------------------------------------------
"""
__author__ = 'simplefly'
# A WSGI callable built using Werkzeug.

import time
from werkzeug.wrappers import Response, Request

@Request.application
def app(request):
    host = request.host
    if ':' in host:
        host, port = host.split(':', 1)
    if request.method != 'GET':
        return Response('501 Not Implemented', status=501)
    elif host != '127.0.0.1' or request.path != '/':
        return Response('404 Not Found', status=404)
    else:
        return Response(time.ctime())