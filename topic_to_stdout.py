#! /usr/bin/env python

import rospy
from std_msgs.msg import Int16
import sys

left = 0
right = 0

def write():
	global left
	global right

	sys.stdout.write("{0} {1}\n".format(left, right))
	sys.stdout.flush()

def set_left(msg):
	global left
	left = msg.data
	write()

def set_right(msg):
	global right
	right = msg.data
	write()

rospy.init_node("topic_to_pipe")

left_sub = rospy.Subscriber("/left", Int16, set_left)
right_sub = rospy.Subscriber("/right", Int16, set_right)

rospy.spin()