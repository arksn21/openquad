#!/usr/bin/env python

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
        print("Offboard Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def talker():
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
        required_position.type_mask = int('010111111000', 2)

        pub.publish(required_position)
        rate.sleep()

    # change the mode to offboard after publishing some position messages
    offboard_mode()

    while not rospy.is_shutdown():

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("Ascending")
                    ascending = True

                if event.key == pygame.K_s:
                    print("Descending")
                    descending = True

                if event.key == pygame.K_UP:
                    print("Forward")
                    forward = True

                if event.key == pygame.K_DOWN:
                    print("Backward")
                    backward = True

                if event.key == pygame.K_LEFT:
                    print("Roll Left")
                    roll_left = True

                if event.key == pygame.K_RIGHT:
                    print("Roll Right")
                    roll_right = True

                if event.key == pygame.K_a:
                    print("Yaw Left")
                    yaw_left = True

                if event.key == pygame.K_d:
                    print("Yaw Right")
                    yaw_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    print("Ascending")
                    ascending = False

                if event.key == pygame.K_s:
                    print("Descending")
                    descending = False

                if event.key == pygame.K_UP:
                    print("Forward")
                    forward = False

                if event.key == pygame.K_DOWN:
                    print("Backward")
                    backward = False

                if event.key == pygame.K_LEFT:
                    print("Roll Left")
                    roll_left = False

                if event.key == pygame.K_RIGHT:
                    print("Roll Right")
                    roll_right = False

                if event.key == pygame.K_a:
                    print("Yaw Left")
                    yaw_left = False

                if event.key == pygame.K_d:
                    print("Yaw Right")
                    yaw_right = False

            if ascending:
                required_position.position.z = required_position.position.z + 0.5

            if descending:
                required_position.position.z = required_position.position.z - 0.5

            if forward:
                required_position.position.y = required_position.position.y + 0.5

            if backward:
                required_position.position.y = required_position.position.y - 0.5

            if roll_left:
                required_position.position.x = required_position.position.x - 0.5

            if roll_right:
                required_position.position.x = required_position.position.x + 0.5

            if yaw_left:
                required_position.yaw = required_position.position.z - 0.5

            if yaw_right:
                required_position.yaw = required_position.position.z + 0.5       

        pygame.display.flip()

        required_position.coordinate_frame = 1
        required_position.type_mask = int('010111111000', 2)

        pub.publish(required_position)
        rate.sleep()
            

if __name__ == '__main__':
    try:
        arm()
        talker()
    except rospy.ROSInterruptException:
        pass



    