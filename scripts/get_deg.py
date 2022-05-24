#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

if __name__ == '__main__':
	rospy.init_node('get_deg')
	pub = rospy.Publisher("/deg_topic", Float64, queue_size=10)
	freq = 0.2
	rate = rospy.Rate(freq)
	while not rospy.is_shutdown():
		deg = Float64()
		deg.data = rospy.get_param("/degrees")
		pub.publish(deg)
		rate.sleep()
	rospy.loginfo("Node stopped")
	

