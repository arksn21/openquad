#! /usr/bin/env python

import rospy

from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
pub = None

def clbk_sonar(msg):
	#regions=[min(msg.ranges[0:9],min(msg.ranges[10:19])]
	take_action(msg.range)
    
def take_action(dist):
    msg = Twist()
    linear_x = 0
    angular_z = 0
    
    state_description = ''
    
    if dist<1:
	linear_x=0
	angular_z=0.8
    else:
        state_description = 'Free path'
	linear_x=1
	angular_z=0
        

    rospy.loginfo(state_description)
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub.publish(msg)

def main():
    global pub
    
    rospy.init_node('sonar_reading')
    
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    sub = rospy.Subscriber('/m2wr/sonar/scan', Range, clbk_sonar)
    
    rospy.spin()

if __name__ == '__main__':
    main()

