#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import math

count = 0

def receive_news_cb(deg): #call back function
	rad = math.radians(deg.data)
	rospy.loginfo(f"{deg.data}, -> {rad}")

if __name__ == '__main__':
	rospy.init_node('deg2rad')
	sub = rospy.Subscriber("/deg_topic", Float64, receive_news_cb)
	rospy.spin()
