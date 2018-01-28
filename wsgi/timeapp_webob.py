# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     timeapp_webob
   Description :
   Author :       simplefly
   date：          2018/1/28
-------------------------------------------------
   Change Activity:
                   2018/1/28:
-------------------------------------------------
"""
__author__ = 'simplefly'
# A WSGI callable built using webob.

import time, webob

def app(environ, start_response):
    request = webob.Request(environ)
    if environ['REQUEST_METHOD'] != 'GET':
        response = webob.Response('501 Not Implemented', status=501)
    elif request.domain != '127.0.0.1' or request.path != '/':
        response = webob.Response('404 Not Found', status=404)
    else:
        response = webob.Response(time.ctime())
    return response(environ, start_response)