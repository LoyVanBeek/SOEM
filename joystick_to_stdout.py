#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import os, sys

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

wheel_separation_multiplier_ = 1
wheel_separation_ = 0.20
wheel_radius_multiplier_ = 1
wheel_radius_ = 0.03

hardware_scaling_factor = 75

def write(twist):
    ws = wheel_separation_multiplier_ * wheel_separation_
    wr = wheel_radius_multiplier_     * wheel_radius_

    vel_left  = (twist.linear.x - twist.angular.z * ws / 2.0)/wr
    vel_right = (twist.linear.x + twist.angular.z * ws / 2.0)/wr

    vel_left *= hardware_scaling_factor
    vel_right *= hardware_scaling_factor

    sys.stdout.write("{0} {1}\n".format(int(vel_left), int(vel_right)))
    # sys.stdout.flush()

rospy.init_node("topic_to_pipe")

cmd_vel_sub = rospy.Subscriber("/cmd_vel", Twist, write)

rospy.spin()