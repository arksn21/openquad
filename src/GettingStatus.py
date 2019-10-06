#!/usr/bin/env python
import rospy
from mavros_msgs.msg import State

def state_get(data):
    print("\nConnected: {} \nArmed: {} \nMode: {}".format(data.connected , data.armed , data.mode))

def listener():
    rospy.init_node('getting_status_node', anonymous=True)
    rospy.Subscriber("/mavros/state", State, state_get)
    rospy.spin()


if __name__ == '__main__':
    listener()