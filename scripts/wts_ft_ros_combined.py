#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script reads three tactile sensors and registers the readings onto the respective topics to be received by respective listening nodes
Due to possible loss of data during transmission, each serial port is looked into one at a time  
"""
import wts_ft_interface as wtsft
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import numpy as np
#===============================================================================
# METHODS
#===============================================================================
PORT = '/dev/ttyACM'

def testGetSensors(port):
    return wtsft.getSensorValues(port)
#===============================================================================
# MAIN METHOD AND TESTING AREA
#===============================================================================

#if __name__ == '__main__':
#    serialFlag=True
#    if serialFlag==True:
#        #runTestCRC()
#        sensor=wtsft.getSensorType(PORT)
#        print "The following sensor", sensor, "was found in", PORT
#        #print "S sensor=getSensorType(PORT)
#        print "Sensor Temperature:", wtsft.getSensorTemperature(PORT)
#        testGetSensors()   

def talker():
    rospy.init_node('pub_sensor1', anonymous=True)
    #pub = rospy.Publisher('wtsft_sensor1', numpy_msg(Floats), queue_size=10)
    
    rate = rospy.Rate(100) # 10hz
    i=0
    while not rospy.is_shutdown():
        for i in range (3):
		try:	
			if i == 0:
				pub = rospy.Publisher('wtsft_sensor1', numpy_msg(Floats), queue_size=1)
			elif i == 1:
				pub = rospy.Publisher('wtsft_sensor2', numpy_msg(Floats), queue_size=1)
			elif i == 2:
				pub = rospy.Publisher('wtsft_sensor3', numpy_msg(Floats), queue_size=1)
			
			sensorArray = np.array(testGetSensors(PORT+str(i)),dtype=np.float32)
			#rospy.loginfo(sensorArray)
			#temperature = wtsft.getSensorTemperature(PORT+str(i))
			#rospy.loginfo(temperature)
			pub.publish(np.array([i],dtype=np.float32))
			pub.publish(sensorArray.reshape(wtsft.SX*wtsft.SY))
			rate.sleep()
		except:
			print("connection error")

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
