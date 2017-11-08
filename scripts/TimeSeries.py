#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
=================
Real time time series of sensor values
=================
"""
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import numpy as np
import wts_ft_interface as wtsft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as plticker
import colormaps as cmaps #small library for plasma colormap
import time

fig, ax = plt.subplots(figsize=(30,7))
global array_fix
array_fix = np.zeros(shape=(8,4))

def update_line():

    tNow = time.time()

    t = np.linspace(tNow - 10.0, tNow, 200)


    line1.set_data(t - tNow, array_fix[0])
    line2.set_data(t - tNow, array_fix[1])

    return (line1, line2)




def callback(data):
	array=np.array(data.data, dtype=np.float32)
	if array.shape[0]==1:
		print "Sensor",int(array[0])
	else:
		array_fix=array.reshape((wtsft.SX,wtsft.SY))
		#update_line()
		plt.plot(array[0])
		fig.show()

def listener():
	rospy.init_node('animatedPlot')
	rospy.Subscriber('wtsft', numpy_msg(Floats), callback)
	
  
    
if __name__ == '__main__':


	(fig, axes_list) = plt.subplots(2, 1)

	axes1 = axes_list[0]
	axes2 = axes_list[1]

	line1, = axes1.plot([], [], 'r-')
	line2, = axes2.plot([], [], 'b-')

	for ax in [axes1, axes2]:
	    ax.set_xlim(-10, 0)
	    ax.set_ylim(-1, 1)
	    #ax.set_xlabel('x')
	    #ax.set_ylabel('y')
	    #ax.set_title('test')
	
	animation = animation.FuncAnimation(fig, update_line, interval = 0, blit = True)
	# Enter the event loop
	fig.show()
	listener()
	rospy.spin()
	
	
    
