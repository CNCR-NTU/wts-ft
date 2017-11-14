# WeissTactile

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

