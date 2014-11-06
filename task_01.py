#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    '''put variables into a dict'''
    try:
        return var1[var2]
    except LookupError:
        print "Warning: Your index/key doesn't exist."
        return var1