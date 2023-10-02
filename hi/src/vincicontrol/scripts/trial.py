#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("testnode")
    rospy.loginfo("bello banana")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("underwear")
        rate.sleep()
    
rospy.sleep(1.0)
rospy.loginfo("poopaye")