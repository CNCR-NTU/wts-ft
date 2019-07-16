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

![](https://github.com/pedrombmachado/biotac_sp/blob/master/doc/Biotac.png)

Figure 1: Biotac setup
  
## Step 2: Update the OS and install base packets

```
$ sudo apt update & sudo apt upgrade -y & sudo apt dist-upgrade -y & sudo apt autoremove -y & sudo apt autoclean -y
$ sudo apt install build-essential git terminator
```

## Step 3: clone the repository
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/CNCR-NTU/biotac_sp_ros.git
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

`$ roslaunch biotac.launch`


# Understanding the data








Simple ROS Package for Weiss tactile sensors. 
Library developed by Pedro Machado. Visualisation by Nikesh

The tactie sensor reading is a 8X4 matrix with each element represented with 16bit unsigned ints. Hence,the value can go from 0 to 65536. The values are shown as heatmaps in real time. 

The current repo consists for three tactile sensors runninng simultaneously.to test with just one tactile; just comment out the for loop in wts_ft_ros_combined.py to go through just one ttyACM connection. 

## Download

Download this repository with the following commands:
```
roscd ; 
cd ../src
https://github.com/LamaNIkesh/WeissTactile.git
cd ..
catkin_make
```

## Usage
To run all three nodes each representing one tactile sensor.
```
roslaunch wts_ft tactile.launch
```


![heatmap](https://user-images.githubusercontent.com/13660762/32507951-b98aeba6-c3e0-11e7-84e5-1ec11b93e46b.png)

