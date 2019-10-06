#!/usr/bin/env python

import sys
import rospy
from mavros_msgs.msg import *
from mavros_msgs.srv import *

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
        
def disarm():
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        armService = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        success = armService(False)
        if (success.success == True):
            print("Disarmed")
        else:
            print("Disarming Failed") 
    except rospy.ServiceException, e:
        print ("Disarming Service Unavailable: %s"%e)

def menu():
    print ("\nRequesting Command")
    print("1. Arm")
    print("2. Disarm")
    print("3. Exit\n")

def menu_selection():
    # initializing the drone in manual mode
    cmd_input=2

    while((not rospy.is_shutdown()) and (cmd_input <= 3)):
        menu()
        cmd_input=int(raw_input("Enter the mode: "))

        if(cmd_input==1):
            arm()
        elif(cmd_input==2):
            disarm()
        else: 
            print "Exit"
            break

if __name__ == "__main__":
    rospy.init_node('command', anonymous=True)
    menu_selection()
