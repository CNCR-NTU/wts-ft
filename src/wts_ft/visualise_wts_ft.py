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
__file_name__ = 'visualiseWts-ft.py'
__description__ = 'Subscribe the Biotac sensors raw data and display the data per sensor'
__compatibility__ = "Python 2 and Python 3"
__platforms__ = "i386, x86_64, arm32 and arm64"
__diff__= "GPLv3 , new lauch file and publication in 3 topics"

#===============================================================================
# IMPORT STATEMENTS
#===============================================================================
import rospy
from std_msgs.msg import String
import numpy as np
import cv2
import os
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg

#===============================================================================
# GLOBAL VARIABLES DECLARATIONS
#===============================================================================
PATH=os.path.dirname(os.path.realpath(__file__))
P=0.98
visualisationFlag = True# False #
SY = 4                           # Num of Sensor columns
SX = 8                          # Num of Sensor rows
scale_percent = 6000  # percent of original size

#===============================================================================
# METHODS
#===============================================================================
def callback_wts_ft(data, publishers):
    global flag, prev_mat, fsr
    wts_ft_array = data.data
    wts_ft_array=wts_ft_array.reshape((SX,SY,3))

    for sensor in range(0, 3):
        aux=wts_ft_array[:,:,sensor].astype(np.uint8)
        if visualisationFlag:
            width = int(aux.shape[1] * scale_percent / 100)
            height = int(aux.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            aux = cv2.resize(aux, dim, interpolation=cv2.INTER_AREA)
            im_color = (cv2.applyColorMap(aux, cv2.COLORMAP_HOT))
            cv2.imshow("Sensor " + str(sensor), im_color)
            publishers[sensor].publish(wts_ft_array[:,:sensor].flatten('F'))
            print(wts_ft_array[:,:sensor])

    if visualisationFlag and cv2.waitKey(1) & 0xFF == ord('q'):
        rospy.signal_shutdown('Quit')
        cv2.destroyAllWindows()


def listener():
    global flag
    while not rospy.is_shutdown():
        try:
            pub0 = rospy.Publisher('sensors/wts_ft/0', numpy_msg(Floats), queue_size=10)
            pub1 = rospy.Publisher('sensors/wts_ft/1', numpy_msg(Floats), queue_size=10)
            pub2 = rospy.Publisher('sensors/wts_ft/2', numpy_msg(Floats), queue_size=10)
            print("Sensor 0 published in topic: /sensors/wts_ft/0.")
            print("Sensor 1 published in topic: /sensors/wts_ft/1.")
            print("Sensor 2 published in topic: /sensors/wts_ft/2.")
            rospy.Subscriber("/sensors/wts_ft/raw", numpy_msg(Floats), callback_wts_ft, ([pub0, pub1, pub2]))
            flag=True
            rospy.spin()
        except rospy.ROSInterruptException:
            print("Shuting down the Biotac subscriber!")
        except IOError:
            print(IOError)
            print("Shuting down the Biotac subscriber!")
#===============================================================================
#  TESTING AREA
#===============================================================================

#===============================================================================
# MAIN METHOD
#===============================================================================
if __name__ == '__main__':
    print("[Initialising wts_ft visualisation...]\n")
    rospy.init_node('visualise_wts_ft', anonymous=True)
    fsr=0
    # if not flag:
    #     main()
    #     flag = True
    listener()
