#!/usr/bin/python
import sys
import time
import logging
import requests
import settings
import random

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
                      - token - token needed to talk to the backend
    Output: 'OK'
    Error: 4xx http error
    Note: 
    """
    headers = {"content-type":"application/json;charset=UTF-8","X-Auth-Token":str(input_dict['token'])}
    data = "{'reading':'65','reading_type':'temp','sensor_serial':'67676767','reading_unit':'celcious'}"
    #get a token from the backend API to send reading data
    url = 'http://'+backend_api+'/api/'+settings.API_VERSION+'/reading'
    try:
        r = requests.post(url,headers=headers, data=data )
        out = r.raise_for_status()
        if(out != None):
            raise Exception('Could not authenticate DHT 11 to backend API')
    except Exception as e:
        print e

    return 'OK'
    #return json.loads(r.text)

def get_sensor(serial):
    """
    Desc: Get the info for a sensor
    Input: None
    Output: Uniqe integer serial
    Error: ERROR
    Note: None
    """