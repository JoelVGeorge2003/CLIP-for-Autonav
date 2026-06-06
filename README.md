# CLIP-for-Autonav

//T1 bringup file
cd ~/catkin_ws
source devel/setup.bash
export TURTLEBOT3_MODEL=waffle_pi
roslaunch turtlebot3_bringup turtlebot3_robot.launch\

//T2 
cd ~/catkin_ws
source devel/setup.bash
export TURTLEBOT3_MODEL=waffle_pi

//make sure every topic exists
rostopic list

//check lidar and odom
rostopic echo /scan

rostopic echo /odom

//make sure cam driver exists
sudo apt install -y ros-noetic-usb-cam

//created cam node
cd ~/catkin_ws/src
catkin_create_pkg tb3_clip_nav rospy sensor_msgs std_msgs geometry_msgs cv_bridge
cd tb3_clip_nav
mkdir -p scripts
nano scripts/opencv_camera_pub.py

//catkin make
chmod +x ~/catkin_ws/src/tb3_clip_nav/scripts/opencv_camera_pub.py
cd ~/catkin_ws
catkin_make
source devel/setup.bash

//run opencv code
rosrun tb3_clip_nav opencv_camera_pub.py _device:=0
