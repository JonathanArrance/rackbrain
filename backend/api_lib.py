from flask import  jsonify,abort,render_template, redirect, url_for
from mongo_lib import Reading as Reading
from mongo_lib import RackBrainSys as RBS
import re

def add_reading(params):
    """
    Add a reading to the database from a sensor. Sensor must be attached and valid.
    input: Params dict - reading - the measured reding from the sensor
                                 - reading_type - the unit the reading is measured in - ['temp','humidity','power','pressure'].
                                 - reading_unit - the units the reading is measured in
                                 - sensor_serial - the unique serial number for the sensor
    output: 201 on successful add
                out_dict - id - unique id of reading
                             - time - time the reading was recorded
    error: 400 no user found
              409 duplicate user
   note: rid - generated unique
            rtime - generated timestamp
    """
    #{'reading_type':reading_type,'reading':reading,'sensor_serial:sensorserial}
    if params is None:
        abort(400)
    if params['reading_type'] is None or params['reading'] is None or params['sensor_serial'] is None or params['reading_unit'] is None:
        abort(400)    # missing arguments

    #TODO: Add sensor validity check
    # mongo_lib.check this sensor if it is in system.
    #if not abort - sensor not attached error
    
    print params
    #reading = Reading(reading=params['reading'],reading_type=params['reading_type'],sensor_serial=params['sensor_serial'],reading_unit=params['reading_unit'])
    #rid = reading.readingid()
    #rtime = reading.readingtime()
    #reading.save()

    return (jsonify({'id': rid,'time':rtime}), 201)

'''
def get_status(userid):
    """
    Return the user based on the userid
    input: userid
    output: dict - username
                     - role
                     - userid
    error: 400 no user found
    """
    if Account.query.filter_by(userid=userid).first() is None:
        abort(400)   # no user found

    user = Account.query.filter_by(userid=userid).first()
    user_spec = AccountSpecs.query.filter_by(userid=userid).first()

    return (jsonify({'username':user.username,'role':user.role,'userid':user.userid,'firstname':user_spec.firstname,'lastname':user_spec.lastname,'email':user_spec.email}),200)
'''