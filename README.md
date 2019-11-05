# WTS-FT

This repository is for hosting the WTS-FT sensors software released under the lgpl3.0 license.

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

## Step 4: compile and install
```
$ cd ~/catkin_ws
$ catkin_make
$ catkin_make install
$ source devel/setup.sh
```

## Step 5: run the lauch files

publisher on the RPI

`$ roslaunch wts_ft_publisher.launch`

visualisation on the host pc

`$ roslaunch visualise_wts_ft.launch`

# Howto cite?
```
@software{machado_pedro_2019_3529664,
  author       = {Machado, Pedro and
                  McGinnity, T.M.},
  title        = {WTS-FT ROS package},
  month        = nov,
  year         = 2019,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.3529664},
  url          = {https://doi.org/10.5281/zenodo.3529664}
}
```



# Contacts

Computational Neurosciences and Cognitive Robotics Group at the Nottingham Trent University.

* Pedro Machado pedro.baptistamachado@ntu.ac.uk

* Martin McGinnity martin.mcginnity@ntu.ac.uk





