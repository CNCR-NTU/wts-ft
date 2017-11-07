#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import numpy as np
import wts_ft_interface as wtsft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as plticker
import colormaps as cmaps #small library for plasma colormap

fig, ax = plt.subplots(figsize=(10,20))
global array_fix
array_fix = np.zeros(shape=(8,4))
 

def callback(data):
	array=np.array(data.data, dtype=np.float32)
	if array.shape[0]==1:
		print "Sensor",int(array[0])
	else:
		#f=open('test9.bin', 'a+b')
		#np.save(f,array)
		#f.close()  
		#print('Raw array: {}'.format(array))      
		array_fix=array.reshape((wtsft.SX,wtsft.SY))
		#updating the array for heatmap
		im.set_data(array_fix)
		plt.draw()
		if(np.amax(array_fix) > int(62000)):
			#just a friendly message
			plt.title("Too strong", color = 'red')
			print("Too strong!!!!!!!!!!!!!!!!!!!!!")
		else:
			plt.title("Reading Pressure", color = 'white')
		#ax.cla()
#main listening function 
#the sensro readings are published in wtsft topic       
def listener():
	rospy.init_node('listener')
	rospy.Subscriber('wtsft', numpy_msg(Floats), callback)
	#ani = animation.FuncAnimation(fig,callback,frames = 400,interval=10 ,blit =True)
	plt.show()	
	rospy.spin()
    
    
if __name__ == '__main__':
	im = ax.imshow(array_fix, interpolation = "nearest", cmap = cmaps.plasma,vmax = 80000)
	#ax.set_facecolor('black')
	fig.patch.set_facecolor('black')
	#setting grid like structure
	ax.set_xticks(np.arange(0, 4, 1));
	ax.set_yticks(np.arange(0, 8, 1));

	# Labels for major ticks
	ax.set_xticklabels(np.arange(1, 5, 1));
	ax.set_yticklabels(np.arange(1, 9, 1));

	# Minor ticks
	ax.set_xticks(np.arange(0.5, 4, 1), minor=True);
	ax.set_yticks(np.arange(0.5, 8, 1), minor=True);

	# Gridlines based on minor ticks
	ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
	##########################################################
	##this bit is only to get white text on the legend
	#if using default black text, just use: plt.colorbar(im)

	cbar = fig.colorbar(im)
	cbar.set_label('Pressure Readings', color = "white")

	# update the text 
	t = cbar.ax.get_yticklabels();
	labels = [item.get_text() for item in t]
	cbar.ax.set_yticklabels(labels, color = 'white')
	################################################################
	plt.draw()
	#calling listenere
	listener()
    
