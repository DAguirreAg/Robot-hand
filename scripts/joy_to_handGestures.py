
import rospy
from robot_hand.srv import *



def callback(data):

    # Send command when a button is pressed
    buttons = data.XXX

    button_id = 1
    rospy.wait_for_service('hand_gesture')
    try:
        hand_gesture = rospy.ServiceProxy('hand_gesture', HandGesture)
        resp1 = hand_gesture(button_id)
        print("Done")
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    

    


def joy_to_handGestures():
    rospy.init_node('joy_to_handGestures')

    # Set up subscriber
    rospy.Subscriber("joy_buttons", String, callback)
    
    print "Ready to send commands"
    rospy.spin()    



if __name__ == "__main__":
    joy_to_handGestures()













