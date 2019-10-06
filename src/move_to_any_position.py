#!/usr/bin/env python

import sys
import rospy
from mavros_msgs.msg import *
from mavros_msgs.srv import *
from geometry_msgs.msg import * 

def arm():
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        armService = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        success = armService(True)
        if (success.success == True):
            print("Armed")
        else:
            print("Arming Failed")    
    except rospy.ServiceException, e:
        print ("Arming Service Unavailable: %s"%e)

def offboard_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='OFFBOARD')
        print(isModeChanged)
        print("Offboard Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def talker():
    pub = rospy.Publisher('/mavros/setpoint_raw/local', PositionTarget, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    i = 0
    while not rospy.is_shutdown():
        i = i+1
        required_position = PositionTarget()

        required_position.position.x = 0.0
        required_position.position.y = 0.0
        required_position.position.z = 2.0

        required_position.coordinate_frame = 1
        required_position.type_mask = int('010111111000', 2)

        pub.publish(required_position)
        rate.sleep()

        # change the mode to offboard after publishing some position messages
        if i == 10:
            offboard_mode()

if __name__ == '__main__':
    try:
        arm()
        talker()
    except rospy.ROSInterruptException:
        pass