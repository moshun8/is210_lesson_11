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
    # try:
    #     if age < 0:
    #         raise InvalidAgeError
    #     elif age >= 0:
    #         return age
    # except InvalidAgeError:
    #     print "Pick a year in the past."
    #     return age
print get_age(1999)
print get_age(2099)