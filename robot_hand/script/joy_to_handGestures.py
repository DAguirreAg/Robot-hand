#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64

pub1 = rospy.Publisher("command1", Float64, queue_size=10)
pub2 = rospy.Publisher("command2", Float64, queue_size=10)
pub3 = rospy.Publisher("command3", Float64, queue_size=10)
pub4 = rospy.Publisher("command4", Float64, queue_size=10)
pub5 = rospy.Publisher("command5", Float64, queue_size=10)
pub6 = rospy.Publisher("command6", Float64, queue_size=10)
pub7 = rospy.Publisher("command7", Float64, queue_size=10)
pub8 = rospy.Publisher("command8", Float64, queue_size=10)
pub9 = rospy.Publisher("command9", Float64, queue_size=10)
pub10 = rospy.Publisher("command10", Float64, queue_size=10)
pub11 = rospy.Publisher("command11", Float64, queue_size=10)
pub12 = rospy.Publisher("command12", Float64, queue_size=10)
pub13 = rospy.Publisher("command13", Float64, queue_size=10)
pub14 = rospy.Publisher("command14", Float64, queue_size=10)
pub15 = rospy.Publisher("command15", Float64, queue_size=10)


# Gestures
def wide():
    # Prepare the joints data
    positions = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # Send commands
    print("Gesture: Wide")
    sendCommands(positions)

def fist():
    # Prepare the joints data    
    positions = [0,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708]

    # Send commands
    print("Gesture: Fist")
    sendCommands(positions)

def thumbsUp():
    # Prepare the joints data
    positions = [0,0,0,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708]
    
    # Send commands
    print("Gesture: ThumbsUp")
    sendCommands(positions)
    
def countDown():
    # Prepare the joints data
    positions = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    # Send commands
    print("Gesture: Count down")
    print("Five,...")
    sendCommands(positions)  
    
    print("Four,...")
    rospy.sleep(2.0)
    positions = [0,1.5708,1.5708,0,0,0,0,0,0,0,0,0,0,0,0]
    sendCommands(positions)  
    
    print("Three,...")
    rospy.sleep(2.0)
    positions = [0,1.5708,1.5708,1.5708,1.5708,1.5708,0,0,0,0,0,0,0,0,0]
    sendCommands(positions)  
    
    print("Two,...")
    rospy.sleep(2.0)
    positions = [0,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,0,0,0,0,0,0]
    sendCommands(positions)  
    
    print("One,...")
    rospy.sleep(2.0)
    positions = [0,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,0,0,0]
    sendCommands(positions) 
    
    print("ZERO!!")
    rospy.sleep(2.0)
    positions = [0,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708]
    sendCommands(positions) 
     

def sendCommands(positions):
    
    pub1.publish(positions[0])
    pub2.publish(positions[1])
    pub3.publish(positions[2])
    pub4.publish(positions[3])
    pub5.publish(positions[4])
    pub6.publish(positions[5])
    pub7.publish(positions[6])
    pub8.publish(positions[7])
    pub9.publish(positions[8])
    pub10.publish(positions[9])
    pub11.publish(positions[10])
    pub12.publish(positions[11])
    pub13.publish(positions[12])
    pub14.publish(positions[13])
    pub15.publish(positions[14]) 
    
def callback(data):

    #Extract data
    axes = data.axes 
    buttons = data.buttons 
    
    # Check which button is pressed
    i = 0
    gesture_id = 0    
    for button in buttons:
        i = i + 1
        if button == 1:
            gesture_id = i
    
    # Send the commands
    if gesture_id == 1:
        wide()
    elif gesture_id == 2:
        fist()
    elif gesture_id == 3:
        thumbsUp()        
    elif gesture_id == 4:
        countDown()
    
def joy_to_handGestures():
    rospy.init_node("joy_to_handGestures")

    # Set up subscriber to the joystick
    rospy.Subscriber("joy", Joy, callback)

    rate = rospy.Rate(10) # 10hz
    rospy.spin()

if __name__ == "__main__":
    joy_to_handGestures()
