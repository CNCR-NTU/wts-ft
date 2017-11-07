#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:ABSTRACT:
This application handles the data received from the WTS_FT sensor

:REQUIRES:

:TODO:

:AUTHOR:  Pedro Machado
:ORGANIZATION: Nottingham Trent University
:CONTACT: pedro.baptistamachado@ntu.ac.uk
:SINCE: Wed Jun 21 11:41:06 2017
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
__date__ = 'Wed Jun 21 11:41:06 2017'
__version__ = '0.1'
__file_name__='wts_ft_interface_1.py'
__description__='WTS-FT sensors interface'
#===============================================================================
# IMPORT STATEMENTS
#===============================================================================
import struct
import crc16
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

#===============================================================================
# METHODS
#===============================================================================
TXRX_TIMEOUT = 0.025
PORT = '/dev/ttyACM1'
PORT_PARAMS = '115200'           # Serial port parameters
WTS_SET_FRONTEND_GAIN ='36'      # Parameter: 8bit uint
WTS_GET_SINGLE_FRAME = '20'     # Parameter: 0 (uncompressed) / 1 (RLE-compressed)
WTS_START_PERIODIC_ACQ = '21'    # Parameter: 1/0 (RLE/uncompressed), 2-byte Intervall in ms
WTS_STOP_PERIODIC_ACQ = '22'     # No Parameter
WTS_GET_SENSOR_TYPE = '38'       # No Parameter
WTS_GET_TMP = '46'               # Get device temperature
WTS_SET_THRESHOLD = '34'         # Parameter: 16bit int
MAX_DAQ = 4095                   # Maximum value ADC
SY = 4                           # Num of Sensor columns
SX = 8                          # Num of Sensor rows
serialFlag=False


# pepare packet
def prepareacket(command, payload, parameters):
    packet=['AA','AA','AA', command]+payload
    if len(parameters)>0:
        packet+=parameters
    checksum=crc16.crc(packet)
    hexPacket=b''
    for i in range (0,len(packet)):
        hexPacket+=struct.pack(">B",packet[i])
    hexPacket+=checksum
    return hexPacket
    
def getSensorType(port):
    packet=prepareacket(WTS_GET_SENSOR_TYPE,["00","00"],[])
    ser=serial.Serial(port, PORT_PARAMS, timeout=TXRX_TIMEOUT)
    ser.write(packet)
    b=ser.read(50)
    ser.close()        
    return b[len(b)-16:len(b)-2]

def getSensorTemperature(port):
    packet=prepareacket(WTS_GET_TMP,["00","00"],[])
    ser=serial.Serial(port, PORT_PARAMS, timeout=TXRX_TIMEOUT)
    ser.write(packet)
    b=ser.read(50)
    ser.close()
    return int(struct.unpack('<h',b[8:10])[0])*0.1

def getSensorValues(port):
    packet=prepareacket(WTS_GET_SINGLE_FRAME,["01","00"],["00"])
    ser=serial.Serial(port, PORT_PARAMS, timeout=TXRX_TIMEOUT)
    ser.write(packet)
    b=ser.read(80)
    ser.close()
    sensorValues=np.zeros([SX,SY])
    inc=0
    for i in range (0,SX):
        for j in range (0,SY):
            sensorValues[i,j]=int(struct.unpack('>H',b[13+inc*2:15+inc*2])[0])
            inc+=1
    return sensorValues

#===============================================================================
# MAIN METHOD AND TESTING AREA
#===============================================================================
#def runTestCRC():
#    a=['AA','AA','AA','01','02','00', '12', '34']
#    b=crc16.crc(a)
#    print 'TEST 1'
#    if hex(struct.unpack('>H',b)[0])==hex(int('6D66',16)):
#        print 'PASS'
#    else:
#        print 'FAIL'
#    a=['AA','AA','AA','01','00','00']
#    b=crc16.crc(a)
#    print 'TEST 2'
#    if hex(struct.unpack('>H',b)[0])==hex(int('E810',16)):
#        print 'PASS'
#    else:
#        print 'FAIL'
#    a=['AA','AA','AA','06','00','00']
#    b=crc16.crc(a)
#    print 'TEST 3'
#    if hex(struct.unpack('>H',b)[0])==hex(int('9726',16)):
#        print 'PASS'
#    else:
#        print 'FAIL'
#
#def testGetSensors():
#     while True:
#            sensorValues=getSensorValues(PORT)
#            print sensorValues
#            time.sleep(0.1)
#
#if __name__ == '__main__':
#    serialFlag=True
#    if serialFlag==True:
#        #runTestCRC()
#        sensor=getSensorType(PORT)
#        print "The following sensor", sensor, "was found in", PORT
#        #print "S sensor=getSensorType(PORT)
#        print "Sensor Temperature:", getSensorTemperature(PORT)
#        testGetSensors()        
       
            
