#!/usr/bin/env python

# Reference for modes: http://wiki.ros.org/mavros/CustomModes

import sys
import rospy
from mavros_msgs.msg import *
from mavros_msgs.srv import *

def acro_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='ACRO')
        print("Acro Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def altitude_control_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='ALTCTL')
        print("Altitude Control Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def position_control_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='POSCTL')
        print("Position Control Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def offboard_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='OFFBOARD')
        print("Offboard Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def stabilized_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='STABILIZED')
        print("Stabilized Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def rattitude_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='RATTITUDE')
        print("Rattitude Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def mission_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='AUTO.MISSION')
        print("Mission Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def loiter_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='AUTO.LOITER')
        print("Loiter Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def rtl_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='AUTO.RTL')
        print("RTL Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def land_mode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='AUTO.LAND')
        print("Land Flight Mode")
    except rospy.ServiceException, e:
        print ("Mode Change Failed: %s" %e)

def menu():
    print ("\nRequesting Mode Change")
    print("1. Acro")
    print("2. Altitude Control")
    print("3. Position Control")
    print("4. Offboard")
    print("5. Stabilized")
    print("6. Rattitude")
    print("7. Mission")
    print("8. Hold")
    print("9. Return")
    print("10. Land")
    print("11. Exit\n")

def menu_selection():
    # initializing the drone in manual mode
    mode_input=1

    while((not rospy.is_shutdown()) and (mode_input <= 14)):
        menu()
        mode_input=int(raw_input("Enter the mode: "))

        if(mode_input==1):
            acro_mode()
        elif(mode_input==2):
            altitude_control_mode()
        elif(mode_input==3):
            position_control_mode()
        elif(mode_input==4):
            offboard_mode()
        elif(mode_input==5):
            stabilized_mode()
        elif(mode_input==6):
            rattitude_mode()
        elif(mode_input==7):
            mission_mode()
        elif(mode_input==8):
            loiter_mode()
        elif(mode_input==9):
            rtl_mode()
        elif(mode_input==10):
            land_mode()
        else: 
            print "Exit"
            break

if __name__ == "__main__":
    rospy.init_node('mode_change', anonymous=True)
    menu_selection()
