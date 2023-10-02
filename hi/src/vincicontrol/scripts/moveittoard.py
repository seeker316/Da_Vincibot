#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import JointState
from std_msgs.msg import Int32MultiArray

def joint_state_callback(data):
    joint_positions = data.position
    joint_positions_degrees = [int(math.degrees(angle)) for angle in joint_positions]

    angle_msg = Int32MultiArray(data=joint_positions_degrees)
    angle_pub.publish(angle_msg)

if __name__ == '__main__':
    rospy.init_node('joint_state_to_degrees', anonymous=True)
    angle_pub = rospy.Publisher('/anglesdegree', Int32MultiArray, queue_size=10)
    rospy.Subscriber('/joint_states', JointState, joint_state_callback)

    rate = rospy.Rate(10)  # Set the publishing rate

    while not rospy.is_shutdown():
        rate.sleep()
