#!/usr/bin/python
import sys
import time
import logging
import requests
import settings

import Adafruit_DHT as ad

LEVELS = {
          'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

def get_backend_token():
        """
        Desc: Get the token from the backend API service
        Input: None
        Output: out_dict - token
                                 - duration - 3600 seconds
        Error: 4xx http error
        Note:
        """
        #get a token from the backend API to send reading data
        url = 'http://'+backend_api+'/api/'+settings.API_VERSION+'/token'
        r = requests.get(url, auth=requests.auth.HTTPBasicAuth(settings.BACKEND_USER, settings.BACKEND_PASS))
        out = r.raise_for_status()
        if(out != None):
            raise Exception('Could not authenticate DHT 11 to backend API')
        return json.loads(r.text)

def send_reading(input_dict):
         """
        Desc: Get the token from the backend API service
        Input: input_dict - reading - the measured reding from the sensor
                                 - reading_type - the unit the reading is measured in - ['temp','humidity','power','pressure'].
                                 - reading_unit - the units the reading is measured in
                                 - sensor_serial - the unique serial number for the sensor 
        Output:
        Error:
        Note: 
        """
        #get a token from the backend API to send reading data
        url = 'http://'+backend_api+'/api/'+settings.API_VERSION+'/reading'
        r = requests.post(url, )
        out = r.raise_for_status()
        if(out != None):
            raise Exception('Could not authenticate DHT 11 to backend API')
        return json.loads(r.text)

 #try:
 #           humidity1, temperature1 = Adafruit_DHT.read_retry(11, int(pin))
 #       except Exception as e:
 #           raise ('Could not get data from DHT11 sensor.')

#class dht11():
 #   def get_reading(pin=None):
#        if(pin == None){
#            raise ('Can not get measurement for DHT11 temp sensor, no pin given.')
#        }
 #       try:
 #           humidity1, temperature1 = Adafruit_DHT.read_retry(11, int(pin))
 #       except Exception as e:
 #           raise ('Could not get data from DHT11 sensor.')
            