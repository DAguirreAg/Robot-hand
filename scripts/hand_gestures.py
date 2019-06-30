
import rospy
from robot_hand.srv import *


# Gestures
def wide():
    # Prepare the joints data

    # Send commands
    print("Gesture: Wide")

def fist():
    # Prepare the joints data

    # Send commands
    print("Gesture: Fist")

def thumbsUp():
    # Prepare the joints data

    # Send commands
    print("Gesture: ThumbsUp")


def handle_HandGesture(gesture_id):

    if gesture_id == 1:
        wide()
    elif gesture_id == 2:
        fist()
    elif gesture_id == 3:
        thumbsUp()

def hand_gestures():
    rospy.init_node('hand_gestures')
    s = rospy.Service('hand_gesture', HandGesture, handle_HandGesture)
    print "Ready to receive commands"
    rospy.spin()    


if __name__ == "__main__":
    hand_gestures()
    
