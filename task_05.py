#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05 module"""


class CustomError(Exception):
    '''makes a custom error with message and cause'''
    def __init__(self, message, cause):
        Exception.__init__(self)
        self.cause = cause