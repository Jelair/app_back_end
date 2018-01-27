# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     squares
   Description :
   Author :       simplefly
   date：          2018/1/26
-------------------------------------------------
   Change Activity:
                   2018/1/26:
-------------------------------------------------
"""
__author__ = 'simplefly'
# Using memcached to cache expensive results.

import memcache, random, time, timeit

def compute_square(mc, n):
    value = mc.get('sq:%d' % n)
    if value is None:
        time.sleep(0.001) # pretend that computing a square is expensive
        value = n * n
        mc.set('sq:%d' % n, value)
    return value

def main():
    mc = memcache.Client(['127.0.0.1:11211'])

    def make_request():
        compute_square(mc, random.randint(0, 5000))

    print('Ten successive runs:')
    for i in range(1, 11):
        print(' %.2fs ' % timeit.timeit(make_request, number=2000), end='')
    print()

if __name__ == '__main__':
    main()