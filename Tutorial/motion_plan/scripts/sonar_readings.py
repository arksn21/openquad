#! /usr/bin/env python

import rospy

from sensor_msgs.msg import Range

def clbk_sonar(msg):
	#regions=[min(msg.ranges[0:9],min(msg.ranges[10:19])]
	rospy.loginfo(msg.range)
def main():
	rospy.init_node('reading_sonar')
	sub=rospy.Subscriber('/m2wr/sonar/scan',Range,clbk_sonar)
	rospy.spin()
if __name__=='__main__':
	main()
