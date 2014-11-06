#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception): pass


def get_age(birthyear):
    age = datetime.datetime.now().year - birthyear

    try:
        if age < 0:
            raise InvalidAgeError
        if age >= 0:
            return age
    except InvalidAgeError:
        print "No negative numbers"
        return age