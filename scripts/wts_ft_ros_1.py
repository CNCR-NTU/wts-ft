#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:ABSTRACT:
WTS-FT support for ROS

:REQUIRES:
ROS Kinect
wts_f_interface
rospy
:TODO:

:AUTHOR:  Pedro Machado
:ORGANIZATION: Nottingham Trent University
:CONTACT: pedro.baptistamachado@ntu.ac.uk
:SINCE: Thu Jun 29 17:50:49 2017
:VERSION: 0.1
 
This file is part of icub-cncr-ntu project.
icub-cncr-ntu project can not be copied and/or distributed without the express
permission of Prof. Martin McGinnity <martin.mcginnity@ntu.ac.uk>

Copyright (C) 2017 All rights reserved, Nottingham Trent University
Computational Neuroscience and Cognitive Robotics Laboratory
email:   pedro.baptistamachado@ntu.ac.uk
website: https://www.ntu.ac.uk/research/groups-and-centres/groups/computational-neuroscience-and-cognitive-robotics-laboratory


"""
#===============================================================================
# PROGRAM METADATA
#===============================================================================
__author__ = 'Pedro Machado'
__contact__ = 'pedro.baptistamachado@ntu.ac.uk'
__copyright__ = 'iCub_cncr_ntu project can not be copied and/or distributed \
without the express permission of Prof. Martin McGinnity <martin.mcginnity@ntu.ac.uk'
__license__ = 'Copyright (C)'
__date__ = 'Thu Jun 29 17:50:49 2017'
__version__ = '0.1'
__file_name__='wts_ft_ros.py'
__description__='WTS FT publisher for ROS Kinect'
#===============================================================================
# IMPORT STATEMENTS
#===============================================================================
import wts_ft_interface_1 as wtsft
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
    pub = rospy.Publisher('wtsft', numpy_msg(Floats), queue_size=10)
    rospy.init_node('pub', anonymous=True)
    rate = rospy.Rate(60) # 10hz
    while not rospy.is_shutdown():
        #for i in range (2,5):
        i=1
        sensorArray = np.array(testGetSensors(PORT+str(i)),dtype=np.float32)
        rospy.loginfo(sensorArray)
        pub.publish(np.array([i],dtype=np.float32))
        pub.publish(sensorArray.reshape(wtsft.SX*wtsft.SY))
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
