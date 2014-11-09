#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 11, current_weather file"""

import urllib2
import json
import csv
import os
from decimal import Decimal


base_url = 'http://api.openweathermap.org/data/2.5/weather'


class CurrentWeatherException(Exception):
    '''what to expect'''

    def __init__(self, code, message):
        super(CurrentWeatherException, self).__init__()
        self.errno = code
        self.message = message


class CurrentWeather(object):
    '''Gets the weather'''
    zip_codes = {}
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def __init__(self, zipcode_data='zipcode_database.csv'):
        self.read_csv(zipcode_data)

    def get_weather(self, city, country, units='metric'):
        '''finds the weather'''
        api_query = '{}?units={}&q={},{}'.format(
            base_url, units, city, country
        )

        try:
            response = urllib2.urlopen(api_query)
        except urllib2.HTTPError, error:
            raise CurrentWeatherException(
                error.code,
                'Error: {} {}'.format(error.code, error.msg))
        finally:
            return json.load(response)['main']
    # print get_weather('New York', 'us')
    # print get_weather('San Francisco', 'us')
    # print get_weather('Austin', 'us')


    def read_csv(self, csv_path):
        '''opens a csv'''
        if not os.path.exists(csv_path):
            raise CurrentWeatherException(
                9010, 'CSV zipcode database {} not found'.format(csv_path))

        try:
            inspect = open(csv_path, 'r')
            report = csv.reader(inspect)
            for line in report:
                lats = Decimal(line[3])
                longs = Decimal(line[4])
                self.zip_codes[line[0]] = {
                    'city': line[1],
                    'state': line[2],
                    # 'latitude': line[3],
                    # 'longitude': line[4],
                    'latitude': lats,
                    'longitude': longs,
                    'country': line[5]}

        except IOError:
            raise CurrentWeatherException(
                4151, 'Error reading {}'.format(csv_path))

        finally:
            if inspect is not None:
                inspect.close()

    def get_city_by_zipcode(self, zipcode):
        '''finds the city name by zip'''
        try:
            return self.zip_codes[zipcode]['city']
        except:
            raise CurrentWeatherException(
                5150, 'Error: Zipcode not found in Zipcode data')

    def get_weather_by_zipcode(self, zipcode):
        '''finds the weather based on the zip'''
        return self.get_weather(
            self.get_city_by_zipcode(zipcode), 'US')