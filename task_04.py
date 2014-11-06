#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04 module"""


class BaseException(Exception):
    '''The Superclass'''
    pass


class StringError(BaseException, TypeError):
    '''String subclassed to BaseException and TypeError'''
    pass


class NumberError(BaseException, TypeError):
    '''NumberError subclassed to BaseException and TypeError'''
    pass


class NonZeroError(NumberError):
    '''subclassed to NumberError'''
    pass