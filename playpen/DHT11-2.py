#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import time
import Adafruit_DHT


# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity1, temperature1 = Adafruit_DHT.read_retry(11, 4)
humidity2, temperature2 = Adafruit_DHT.read_retry(11, 7)
humidity3, temperature3 = Adafruit_DHT.read_retry(11, 8)

# Un-comment the line below to convert the temperature to Fahrenheit.
temperature1 = temperature1 * 9/5.0 + 32
temperature2 = temperature2 * 9/5.0 + 32
temperature3 = temperature3 * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
count = 0
while count <= 60:
    if humidity1 is not None and temperature1 is not None:
        print('Temp1={0:0.1f}*  Humidity1={1:0.1f}%'.format(temperature1, humidity1))
        print('Temp2={0:0.1f}*  Humidity2={1:0.1f}%'.format(temperature2, humidity2))
        print('Temp3={0:0.1f}*  Humidity3={1:0.1f}%'.format(temperature3, humidity3))
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
    time.sleep(10)
    count += 1
    
    
