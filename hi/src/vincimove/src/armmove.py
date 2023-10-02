#! /usr/bin/env python3

import sys
import rospy
import moveit_commander
import geometry_msgs.msg

# Initialize ROS node
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

# Create a RobotCommander instance
robot = moveit_commander.RobotCommander()

# Specify the MoveGroup name
arm_group = moveit_commander.MoveGroupCommander("kinematic")

# Print available MoveGroup names for debugging
print("Available MoveGroups:", robot.get_group_names())

# Set a named target (make sure it's defined in your configuration)
arm_group.set_named_target("pose1")

# Plan and execute the motion
plan1 = arm_group.go()

# Sleep to give time for the motion to complete
rospy.sleep(5)

# Shutdown MoveIt
moveit_commander.roscpp_shutdown()
