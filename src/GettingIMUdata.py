#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu


def callback(data):
    print("\nlinear acceleration:\nx: [{}]\ny: [{}]\nz: [{}]"
    .format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z))

    print("\nangular velocity:\nx: [{}]\ny: [{}]\nz: [{}]"
    .format(data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z))

    print("\norientation:\nx: [{}]\ny: [{}]\nz: [{}]"
    .format(data.orientation.x, data.orientation.y, data.orientation.z))


def listener():
    rospy.init_node('getting_imu_node', anonymous=True)
    rospy.Subscriber("/mavros/imu/data", Imu, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()