#!/usr/bin/env python
import rospy
from sensor_msgs.msg import BatteryState

def battery_get(data):
    print("\nVoltage: {} \nCurrent: {} \nPercentage: {}".format(data.voltage , data.current , data.percentage))

def listener():
    rospy.init_node('getting_battery_node', anonymous=True)
    rospy.Subscriber("/mavros/battery", BatteryState, battery_get)
    rospy.spin()


if __name__ == '__main__':
    listener()