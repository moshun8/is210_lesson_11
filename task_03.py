#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    '''custom logger'''
    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        '''logs'''
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        '''flushes'''
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')

            try:
                for index, entry in enumerate(self.msgs):
                    fhandler.write(str(entry) + '\n')
                    handled.append(index)

            except IOError as ioerr:
                self.log(ioerr)
            finally:
                fhandler.close()

            try:
                for index in handled[::-1]:
                    del self.msgs[index]
            except IOError:
                pass

        except Exception as excep:
            self.log(excep)
            raise