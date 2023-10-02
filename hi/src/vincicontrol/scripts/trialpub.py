#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32MultiArray
if __name__ == '__main__':
    rospy.init_node("trial_publisher")
    rospy.loginfo("this is where the trial_pub starts")

    pub = rospy.Publisher('random_array',Int32MultiArray,queue_size=1)
    rate= rospy.Rate(1)

    while not rospy.is_shutdown():
        randomarray = [random.randint(1,100)for _ in range(5)]
        msg = Int32MultiArray(data=randomarray)

        pub.publish(msg)

        rospy.loginfo(f"Published array: {randomarray}")

        rate.sleep()