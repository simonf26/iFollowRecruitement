# iFollowRecruitement
Recruitement tests for iFollow

#	Introduction
This repository is meant for recruitement for iFollow.
In these tests I have discovered or rediscovered the ROS framework and some of its functionnalities.

The different exercises will be driven and described in this file:

Ubuntu 20.04 and ROS' installation will not be taken in account in the time taken.
These tests have been driven on an Ubuntu 20.04 Virtual Machine because I've had trouble with my personal USB key when installing a dual boot on my computer.

#	1. Mise en place de l’environnement de test  (60-80 minutes)
##	Downloading turtlebot3 packages
$ sudo apt install ros-noetic-dynamixel-sdk	# this package might be useless for the simulation as it is meant for the robots motors
$ sudo apt install ros-noetic-turtlebot3-msgs
$ sudo apt install ros-noetic-turtlebot3

##	Using GAZEBO 
### Follow the following steps: https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation
The following commands are meant to be run in different terminals, each of them should run beforehands: $ export TURTLEBOT3_MODEL=burger

$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping 
###	To Control the robot using keyboard:
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch # This command allows the user to control the robot using their keyboard

Make sure the terminal window is opened while you try to control the robot, otherwise the commands will not be taken in account and the robot won't be moving at all
The RVIZ window will show of view of the map known by the robot, try and visit as much of the map as you can so that the robot can map it entirely
When the map is complete: 
$ rosrun map_server map_saver -f ~/map

###	To Navigate the map you can use: $ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/map_path/map.yaml

###	The map use for this test is available in the "Setting" folder

#	2. Multiplexer (45-60 minutes)
Here I started looking into the code of teleop and turlebot_drive and then while looking for a solution online I found that there was a tool already implemented in topic_tools. But it never is a waste of time to look through code to understand how things work! 

To create a multiplexer:
rosrun topic_tools mux cmd_vel /cmd_local /cmd_web mux:=mux_cmdvel

To switch source to web:
rosrun topic_tools mux_select  cmd_select /cmd_web
or to select local source:
rosrun topic_tools mux_select  cmd_select /cmd_local

#	3. Teleoperation a distance
rostopic pub -r 1 /ROS/cmd_web std_msgs/Int32 









