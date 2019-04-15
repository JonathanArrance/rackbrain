#!/bin/pythonfrom flask import  jsonify,abort,render_template, redirect, url_forfrom mongo_lib import Account as Accountfrom mongo_lib import AccountSpecs as AccountSpecsfrom mongo_lib import SensorInventoryfrom mongo_lib import SensorCatalog as SensorCatalogfrom mongo_lib import Reading as Readingfrom mongo_lib import AttachedDevice as Devicefrom mongo_lib import DeviceCatalog as DeviceCatalogfrom mongo_lib import RackBrainSys as RBSimport re#################USER##################def create_user(params=None):    """    Desc: Create a new user based on the params given    Input: Params dict    Output: 201 on successful add    Error: 400 no user found              409 duplicate user    Note: None
    """    if params is None:        abort(400)    if params['username'] is None or params['password'] is None or params['role'] is None:        abort(400)    # missing arguments    if Account.query.filter_by(username=params['username']).first() is not None:        abort(409)   # existing user    user = Account(username=params['username'])    user.hash_password(params['password'])    userid = user.gen_id()    user.add_role(params['role'])    user.save()    specs = AccountSpecs(userid=userid,lastname='none',email='none',firstname='none')    specs.save()    return (jsonify({'username': user.username,'userid':userid}), 201)def get_user(userid=None):    """    Desc: Return the user based on the userid    Input: userid    Output: dict - username                     - role                     - userid    Error: 400 no user found    Note:
    """    if Account.query.filter_by(userid=userid).first() is None:        abort(400)   # no user found    user = Account.query.filter_by(userid=userid).first()    user_spec = AccountSpecs.query.filter_by(userid=userid).first()    return (jsonify({'username':user.username,'role':user.role,'userid':user.userid,'firstname':user_spec.firstname,'lastname':user_spec.lastname,'email':user_spec.email}),200)def update_user(input_dict=None):    """
    Desc: Update the user info
    Input: 
    Output:    Error:  400 invalid value              404 no user found    Note: 
    """    if Account.query.filter_by(userid=input_dict['userid']).first() is None:        abort(404)   # no user found       #Get the original entry    user = Account.query.filter_by(userid=input_dict['userid']).first()    spec = AccountSpecs.query.filter_by(userid=input_dict['userid']).first()    if('firstname' not in input_dict):        input_dict['firstname'] = 'none'        if('lastname' not in input_dict):        input_dict['lastname'] = 'none'            #check the email address    if('email' in input_dict and input_dict['email'] is not None):        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', input_dict['email'])        if(match == None):            input_dict['email'] = 'none'            if('role' in input_dict and input_dict['role'] is not None):        user.add_role(str(input_dict['role']))            if('password' in input_dict and input_dict['password'] is not None):        user.hash_password(input_dict['password'])        specs = AccountSpecs(userid=int(input_dict['userid']),                         lastname=input_dict['lastname'],                         email=input_dict['email'],                         firstname=input_dict['firstname'])    specs.save()    user.save()    return (201)def list_users():
	"""
	Desc: List the users in the rackbrain
	Input:
	Output:
	Error:
	Note:
	"""    #Return a list of users based on the role given. If no role given all roles returned except internal roles.    #if the role is not given and the role of the user makeing the call is internal return all    users = Account.query.all()    return (users,200)def delete_user(userid=None):
	"""
	Desc: Delete a user in the rackbrian
	Input:
	Output:
	Error:
	Note: Only admins can do this, can not remove the backend service user.
	"""    if(userid == None):        abort(406)            if Account.query.filter_by(userid=input_dict['userid']).first() is None:        abort(404)   # no user found    #Get the original entry    user = Account.query.get_or_404(userid=int(input_dict['userid']))    spec = AccountSpecs.query.get_or_404(userid=int(input_dict['userid']))    user.remove()    spec.remove()    return (200)####################################################READING####################def add_reading(params=None):    """    Desc: Add a reading to the database from a sensor. Sensor must be attached and valid.    Input: Params dict - reading - the measured reding from the sensor                       - reading_type - the unit the reading is measured in - ['temp','humidity','power','pressure'].                       - reading_unit - the units the reading is measured in                       - sensor_serial - the unique serial number for the sensor    Output: 201 on successful add                out_dict - id - unique id of reading                             - time - time the reading was recorded    Error: 400 no user found    Note: rid - generated unique          rtime - generated timestamp    """    #{'reading_type':reading_type,'reading':reading,'sensor_serial:sensorserial}    if params is None:        abort(400)    if params['reading_type'] is None or params['reading'] is None or params['sensor_serial'] is None or params['reading_unit'] is None:        abort(400)    # missing arguments    #TODO: Add sensor validity check    # mongo_lib.check this sensor if it is in system.    #if not abort - sensor not attached error    values = ['temp','humidity','power','pressure']    if str(params['reading_type']).lower() not in values:        abort(400)    reading = Reading(reading=params['reading'],reading_type=params['reading_type'],sensor_serial=params['sensor_serial'],reading_unit=params['reading_unit'])    rid = reading.reading_id()    rtime = reading.reading_time()    reading.save()    return (jsonify({'id': rid,'time':rtime}), 201)def get_readings(reading_id=None):    """
    Desc: Get a reading at a point in time.
    Input: reading_id
    Output: out_dict - reading
    			     - reading_type
    			     - reading_unit
    			     - sensor_serial
    Error: 400 no reading found
    """    passdef get_all_readings(sensor_serial=None):
	"""
	Desc: Get all of the readings for a particular sensor
	Input: sensor_serial
	Output: array of out_dict - reading
				              - reading_type
				              - reading_unit
	Error: 400 no sensor found
	"""    pass###################################################SENSOR####################Sensor API workers#Used to get info from the db in regards to the sensors attached to the rackbraindef attach_sensor(params=None):
	"""
	Desc: Add a new supported sensor to the rack brain sensor inventory.
	Input: params - sensor_name
	              - sensor_type
	Output: out_dict - sensor_serial
	                 - sensor_name
	Notes: Only an admin can add a supported sensor to the rackbrain inventory. 
	       A sensor must be a part of the rackbrain catalog in order to be added to inventory.
	"""    if params is None:        abort(400)    if params['sensor_name'] is None or params['sensor_type'] is None:        abort(400)    # missing arguments    if SensorInventory.query.filter_by(sensorname=params['sensor_name']).first() is not None:        abort(409)   # existing sensor    if SensorCatalog.query.filter_by(sensortype=params['sensor_type']).first() is None:        abort(409)   # sensor type is not in the catalog

	#get the sensor from the catalog
    sensor = SensorInventory(sensorname=params['sensor_name'])    sensor_serial = sensor.sensor_serial()    sensor.sensor_type(params['sensor_type'])    sensor.sensor_desc(params['sensor_desc'])    sensor.save()    return (jsonify({'sensor_name': sensor.sensorname,'sensor_serial':sensorid}), 201)

def add_sensor_to_catalog(params=None):
	"""
	Desc: Add a new supported sensor to the rack brain sensor catalog.
	Input: params - sensor_type
	              - sensor_desc
	              - sensor_id
	Output:
	Error:
	Note: Only an admin can add a supported sensor to the rackbrain catalog. 
	      A sensor must be a part of the rackbrain catalog in order to be used.
	"""
	if params is None:
		abort(400)
	
	#add the sensor to the catalog
	pass
def list_attached_sensors():
	"""
	Desc: List all of the attached sensors.
	Input:
	Output:
	Error:
	Note:
	"""    sensor = SensorInventory.query()    return (sensor,201)def get_attached_sensor(sensor_serial=None):
	"""
	Desc: Get an attached sensor.
	Input:
	Output:
	Error:
	Note: 
	"""    if(sensor_serial is None):        abort(400)    sensor = SensorInventory.query.filter_by(sensor_serial=sensor_serial).first()    return (jsonify({'sensor_name':sensor.sensor_name,                     'sensor_serial':sensor.sensor_serial,                     'sensor_type':sensor.sensor_type,                     'sensor_desc':sensor.sensor_desc}),201)def delete_attached_sensor(sensor_serial=None):
	"""
	Desc: Remove a sensor from the rackbrain.
	Input:
	Output:
	Error:
	Note: 
	"""    if(sensor_serial is None):        abort(400)    sensor = SensorInventroy(sensor_serial=sensor_serial)    sensor.remove()

def delete_sensor(sensorid):
	"""
	Desc: Delete a sensor a supported sensor from the catalog.
	Input:  
	Output:
	Error:
	Note: Only an admin can remove a sensor from the catalog
	"""
	pass    ################################################DEVICE#####################def attach_device(params=None):
	"""
	Desc: Attach a new device, such as a fan, from the device catalog to the rackbrain.
	Input:
	Output:
	Error:
	Note: The device must be in the the device catalog before it can be added.
    """    if params is None:        abort(400)    if params['device_name'] is None or params['device_type'] is None:        abort(400)    # missing arguments    if AttachedDevice.query.filter_by(devicename=params['device_name']).first() is not None:        abort(409)   # existing device    if DeviceCatalog.query.filter_by(devicetype=params['device_type']).first() is None:        abort(409)   # device type is not in the catalog
    if DeviceCatalog.query.filter_by(device_id=params['device_id']).first() is None:
    	abort(409) #The specific device id is not in the catalog    device = AttachedDevice(devicename=params['device_name'])    ds = device.deviceserial()    device.devicetype(params['device_type'])    device.devicedesc(params['device_desc'])    device.save()    return (jsonify({'device_name': device.devicename,'device_serial':ds}), 201)#Attached devices#Devices can be fans, LCD screens, power outlets, etc.def list_attached_devices():
	"""
	Desc: List all of the attached devices
	Input:
	Output:
	Error:
	Note:
	"""    devices = Device.query()    return devicesdef get_attached_device(device_serial):
	"""
	Desc: Get an attached device
	Input:
	Output:
	Error:
	Note:
	"""    if(device_serial is None):        abort(400)    device = Device.query.filter_by(device_serial=device_serial).first()    return (jsonify({'device_name':device.device_name,                     'device_serial':device.device_serial,                     'device_type':device.device_type,                     'device_desc':device.device_desc}),201)def delete_attached_device(device_serial):
	"""
	Desc: Remove an attached device from the rackbrain.
	Input: device_serial
	Output: 200 'OK'
	Error: 400 
	Note: None
	"""    passdef add_device(input_dict):
	"""
	Desc: Add a new supported device to the device catalog
	Input:
    Output:
    Error:
    Note:
	"""    pass

def delete_device(deviceid):
	"""
	Desc: Remove a device from the device catalog
	Input:
	Output:
	Error:
	Note:
	"""
	pass
###############################################LOCATION###################location API workersdef insert_location(input_dict):
	"""
	Desc: Insert the current location of the rackbrain.
	Input:
	Output:
	Error:
	Note:
    """    passdef update_location(input_dict):
	"""
	Desc: Update the location of the rackbrain if different from the location added at setup.
	Input: 
	Output:
	Error:
	Note:
	"""    pass#####################################