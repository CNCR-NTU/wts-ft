# WTS-FT

This repository is for hosting the WTS-FT sensors sofware released under the lgpl3.0 license.

# Requirements

## Documentation
* [WTS-FT Command Set Reference Manual](https://www.weiss-robotics.com/wp-content/uploads/wts_command_set_reference_manual.pdf)
* [WTS-FT Product Data Sheet](https://www.weiss-robotics.com/wp-content/uploads/wts-ft_leaflet_en.pdf)

## Hardware
* 3x WTS-FT sensors
* micro-USB power cable for connecting the rpi
* RPI 3 model B
* Host pc

## Software
* Ubuntu Linux 18.04 LTS (x86_64 and ARM 64 on the the rpi)
* ROS Melodic [installed](http://wiki.ros.org/melodic/Installation/Ubuntu) and [configured](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

# Installation procedure:
## Step 1: Connect the equipment 
Figure 1 shows the configuration setup

![](Documentation/wts-ft.png)

Figure 1: WTS-FT setup
  
## Step 2: Update the OS and install base packets

```
$ sudo apt update & sudo apt upgrade -y & sudo apt dist-upgrade -y & sudo apt autoremove -y & sudo apt autoclean -y
$ sudo apt install build-essential git terminator
```

## Step 3: clone the repository
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/CNCR-NTU/wts_ft.git
```

## Step 4: install the drivers
```
$ cd biotac_sp_ros
$ ./installCheetahDriver.sh
```

## Step 5: compile and install
```
$ cd ~/catkin_ws
$ catkin_make
$ catkin_make install
$ source devel/setup.sh
```

## Step 6: run

Run terminator

`$ roslaunch wts_ft_publisher.launch`


# Understanding the data


# Contacts

Computational Neurosciences and Cognitive Robotics Group at the Nottingham Trent University.

* Pedro Machado pedro.baptistamachado@ntu.ac.uk

* Martin McGinnity martin.mcginnity@ntu.ac.uk







