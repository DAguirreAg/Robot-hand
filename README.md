# Robot-hand
A ROS-Gazebo package to control and simulate a robotic hand.
<p align="middle">
  <img src="/images/Joystick being played.gif" alt="Joystick being played" height=200>
  <img src="/images/Hand doing gestures.gif" alt="Hand doing gestures.gif" height=200>
</p>

## Introduction
The following repository holds a ROS package that simulates a 15DOF robotic hand with some available gestures. The available hand gestures so far are:
1. Open hand
2. Close hand
3. Thumbs up
4. Cound down

## How to get started
Just follow the next steps:

1. Install the package
2. Plug in the joystick
3. Execute `roslaunch launchMe.launch`
4. Wait until Gazebo is loaded
5. Press the joystick's buttons
6. The hand will start doing some gestures

## How it works
There are three main parts you should care look around:

* script: It holds the code for remapping the joystick's keystrokes into gesture commands to be  done by the robot hand.
* urdf: It holds the URDF file that defines the robot hand's dynamics and kinematics.
* launch file: It holds the code that will be executed by roslaunch and it will set up all the nodes and simulation accordingly.

## Getting into details
This repository can be divided into two main components, the simulation and the ROS environment. Below code is for a more in-depth explanation, which you shouldn't care about as it is done automatically by the system when using `roslaunch launchMe.launch`.


### ROS enviroment
For controlling the "robot", we want to pass a some positional commands to control the **15DOF** of the system. As in this case we will be connecting the ROS enviroment to a simulated world, we add the `libgazebo_ros_control.so` plugin to the URDF to allow a communication between ROS and Gazebo and we add some `transmission_interface`s to allow for a **positional control**.

Once the urdf is prepared, we create a simple script ("joy_to_handGestures.py") that converts the readings from a joysticks into an actual commands for the "robot". The reading of the joysticks is handled by the "Joy_node" which is loaded from the ["Joy" ROS package](https://wiki.ros.org/joy). All this gives a result the following graph:

<p align="center">
  <img src="images/Joystick reader-sender setup.jpg" width=600><br/>
  <i>Joystick reader-sender setup</i>
</p>


### Gazebo simulation
The robot hand is composed of **16 links and 15 joints** as seen in below images. 
<p align="middle">
  <img src="/images/Gazebo setup normal view.png" alt="Gazebo setup normal view" >
  <img src="/images/Gazebo setup wireframe view.png" alt="Gazebo setup wireframe view" >
</p>


Once everything is setup, the whole result should be the following (for a more detailed view check [here](https://github.com/DAguirreAg/robot_hand/blob/master/images/Complete%20setup.pdf)):
<p align="center">
  <img src="images/Complete setup.jpg" width=900><br/>
  <i>Complete ROS setup</i>
</p>


## Requirements
You should install the following:
* ROS-lunar
* Gazebo
* Python
* Joy (ROS package)
* USB joystick





