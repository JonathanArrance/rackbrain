#!/usr/bin/python
import sys
import time
import logging
import requests
import Adafruit_DHT

LEVELS = {
          'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

class dht11():
    def get_reading(pin=None):
        if(pin == None){
            raise ('Can not get measurement for DHT11 temp sensor, no pin given.')
        }
        try:
            humidity1, temperature1 = Adafruit_DHT.read_retry(11, int(pin))
        except Exception as e:
            raise ('Could not get data from DHT11 sensor.')
            