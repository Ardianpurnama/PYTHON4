#!/bin/env python
#
# Autogenerated by Thrift Compiler (0.14.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#
# -*- coding: utf-8 -*-

import unittest

class Dict(dict):
    
    def __init__(self, default_value):
        dict.__init__(self)
        self._default_value = default_value
    
    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self._default_value


class Test(unittest.TestCase):

    def test_mydict(self):
        d = Dict("Invalid")
        d[1] = 'one'
        d[2] = 'two'
        self.assertTrue(d[1], 'one')
        self.assertTrue(d[3], 'Invalid')
        

if __name__ == "__main__":
    unittest.main()
