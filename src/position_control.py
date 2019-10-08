#!/usr/bin/env python

###################################################################################################
# Position Control of the Iris Drone with respect to world coordinates

# Controls:
# Use Arrow keys to control the roll and pitch of the drone. 
# Use W to ascend and S to descend. 
# Use A to yaw left and D to yaw right
###################################################################################################

# Gain of the flight controller
gain = 0.5

import sys
import rospy
from mavros_msgs.msg import *
from mavros_msgs.srv import *
from geometry_msgs.msg import * 
import pygame

pygame.init()
windowSize = width,height = 10,10
screen = pygame.display.set_mode(windowSize)


def arm():
    # func to arm the drone
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
    # func to change the flight mode to offboard
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='OFFBOARD')
        print("Offboard Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def talker():
    # function to publish the target position of the drone
    global gain

    ascending = False
    descending = False
    forward = False
    backward = False
    roll_left = False
    roll_right = False
    yaw_left = False
    yaw_right = False

    pub = rospy.Publisher('/mavros/setpoint_raw/local', PositionTarget, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    required_position = PositionTarget()

    for i in range(10):

        required_position.position.x = 0.0
        required_position.position.y = 0.0
        required_position.position.z = 0.0

        required_position.coordinate_frame = 1
        required_position.type_mask = int('000111111000', 2)

        pub.publish(required_position)
        rate.sleep()

    # change the mode to offboard after publishing some position messages
    offboard_mode()

    while not rospy.is_shutdown():

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ascending = True

                if event.key == pygame.K_s:
                    descending = True

                if event.key == pygame.K_UP:
                    forward = True

                if event.key == pygame.K_DOWN:
                    backward = True

                if event.key == pygame.K_LEFT:
                    roll_left = True

                if event.key == pygame.K_RIGHT:
                    roll_right = True

                if event.key == pygame.K_a:
                    yaw_left = True

                if event.key == pygame.K_d:
                    yaw_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    ascending = False

                if event.key == pygame.K_s:
                    descending = False

                if event.key == pygame.K_UP:
                    forward = False

                if event.key == pygame.K_DOWN:
                    backward = False

                if event.key == pygame.K_LEFT:
                    roll_left = False

                if event.key == pygame.K_RIGHT:
                    roll_right = False

                if event.key == pygame.K_a:
                    yaw_left = False

                if event.key == pygame.K_d:
                    yaw_right = False

        if ascending:
            required_position.position.z = required_position.position.z + gain
            print("Ascending")

        if descending:
            required_position.position.z = required_position.position.z - gain
            print("Descending")

        if forward:
            required_position.position.y = required_position.position.y + gain
            print("Forward")

        if backward:
            required_position.position.y = required_position.position.y - gain
            print("Backward")

        if roll_left:
            required_position.position.x = required_position.position.x - gain
            print("Roll Left")

        if roll_right:
            required_position.position.x = required_position.position.x + gain
            print("Roll Right")

        if yaw_left:
            required_position.yaw = required_position.yaw + gain
            print("Yaw Left")

        if yaw_right:
            required_position.yaw = required_position.yaw - gain
            print("Yaw Right")       

        pygame.display.flip()

        required_position.coordinate_frame = 1

        # see mavros msg Position Target for bit masking
        # In this case postion control is enabled
        # mask or unmask all the three x, y & z to take effect
        required_position.type_mask = int('000111111000', 2)

        pub.publish(required_position)
        rate.sleep()
            

if __name__ == '__main__':
    try:
        arm()
        talker()
    except rospy.ROSInterruptException:
        pass



    