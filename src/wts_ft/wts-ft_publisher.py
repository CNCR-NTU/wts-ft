#!/usr/bin/env python
from __future__ import print_function

# -*- coding: utf-8 -*-
"""
:ABSTRACT:
This script is part of the of the enhanced grasp project

:REQUIRES:

:
:AUTHOR:  Pedro Machado
:ORGANIZATION: Nottingham Trent University
:CONTACT: pedro.baptistamachado@ntu.ac.uk
:SINCE: 10/04/2019
:VERSION: 0.1

2019 (c) GPLv3, Nottingham Trent University
Computational Neuroscience and Cognitive Robotics Laboratory
email:  pedro.baptistamachado@ntu.ac.uk
website: https://www.ntu.ac.uk/research/groups-and-centres/groups/computational-neuroscience-and-cognitive-robotics-laboratory


"""
# ===============================================================================
# PROGRAM METADATA
# ===============================================================================
__author__ = 'Pedro Machado'
__contact__ = 'pedro.baptistamachado@ntu.ac.uk'
__copyright__ = '2019 (C) GPLv3, CNCR@NTU, Prof. Martin McGinnity martin.mcginnity@ntu.ac.uk'
__license__ = 'GPLv3'
__date__ = '12/07/2019'
__version__ = '1.0'
__file_name__ = 'wts-ft_publisher.py'
__description__ = 'collects the values from 3 wts-ft and publishes the results on the topics'
__compatibility__ = "Python 2 and Python 3"
__platforms__ = "i386, x86_64, arm32 and arm64"
__diff__ = "GPLv3 , new lauch file and publication in 3 topics"

# ===============================================================================
# IMPORT STATEMENTS
# ===============================================================================
import wts_ft_interface as wtsft
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import numpy as np
import time

# ===============================================================================
# GLOBAL VARIABLES DECLARATIONS
# ===============================================================================
PORT = '/dev/ttyACM'


def getSensorValues(port):
    return wtsft.getSensorValues(port)

def main(publishers):
    while not rospy.is_shutdown():
        sensorsArray = []
        for sensors in range(0, 3):
            sensorsArray.append(np.array(getSensorValues(PORT + str(sensors)), dtype=np.float32))
            print(sensorsArray[sensors])
            publishers[sensors].publish(sensorsArray[sensors].flatten('F'))
        time.sleep(100)



if __name__ == '__main__':
    print("[Initialising wts_ft publisher...]\n")
    rospy.init_node('wts_ft_publisher', anonymous=True)
    try:
        pub0 = rospy.Publisher('sensors/wts_ft/0', numpy_msg(Floats), queue_size=1)
        pub1 = rospy.Publisher('sensors/wts_ft/1', numpy_msg(Floats), queue_size=1)
        pub2 = rospy.Publisher('sensors/wts_ft/2', numpy_msg(Floats), queue_size=1)
        print("Sensor 0 published in topic: /sensors/wts_ft/0.")
        print("Sensor 1 published in topic: /sensors/wts_ft/1.")
        print("Sensor 2 published in topic: /sensors/wts_ft/2.")
        publishers=[pub0,pub1,pub2]
        main(publishers)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
