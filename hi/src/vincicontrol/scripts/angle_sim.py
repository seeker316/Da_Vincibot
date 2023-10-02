#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32MultiArray

mem = [0,0,0,0,0]

def angle_input():
    infotxt = '''Enter the angles for robotic arm wrt the given indexes
                #1 base angle
                #2 shoulder angle
                #3 elbow angle
                #4 wrist rotate angle 
                #5 wrist angle'''
    print(infotxt)
    user_angle_list = [int(input(f"Enter angle #{i + 1}: ")) for i in range(5)]

    print("Entered angles list:", user_angle_list)
    return user_angle_list

def micro_step(angles,n):
            #define the length of a step
    for i,a in enumerate(mem):
        if mem[i]+n < angles[i]:
            # step_angles[i]=n
            mem[i] = mem[i]+n
            
        else:
            mem[i]=angles[i]

    return mem


    

if __name__ == '__main__':
    rospy.init_node("angle_sim")
    rospy.loginfo("angle simulator node started")

    pub = rospy.Publisher('/angles',Int32MultiArray)
    inp = angle_input()

    rate= rospy.Rate(3)
    rospy.loginfo("now printing step angles")

    while not rospy.is_shutdown():
        
        steps = micro_step(inp,5)
        msg = Int32MultiArray(data=steps)

        pub.publish(msg)

        rospy.loginfo(f"Published step angles: {steps}")


        rate.sleep()