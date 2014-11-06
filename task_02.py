#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception): pass


def get_age(birthyear):
    '''put in birth year, get an age'''
    age = datetime.datetime.now().year - birthyear

    if age >= 0:
        return age
    else:
        raise InvalidAgeError