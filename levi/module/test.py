#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

'a test module'

__author__ = 'Levi.Ding'

def test():
    args = sys.argv
    print(args)
    print(__name__)

if __name__ == '__main__':
    print('测试一下')
    test()
