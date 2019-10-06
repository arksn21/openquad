#!/usr/bin/env python
import rospy
from mavros_msgs.msg import Altitude


def altitude_get(data):
    print("\nLocal Altitude: {} \nGlobal Altitude: {}".format(data.local , data.relative))

def listener():
    rospy.init_node('getting_altitude_node', anonymous=True)
    rospy.Subscriber("/mavros/altitude", Altitude, altitude_get)
    rospy.spin()


if __name__ == '__main__':
    listener()