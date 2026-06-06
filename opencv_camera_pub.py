#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node("opencv_camera_pub")

device = rospy.get_param("~device", 0)
width = rospy.get_param("~width", 640)
height = rospy.get_param("~height", 480)

cap = cv2.VideoCapture(device)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

bridge = CvBridge()
pub = rospy.Publisher("/camera/image_raw", Image, queue_size=1)

rate = rospy.Rate(15)

if not cap.isOpened():
    rospy.logerr("Could not open camera device %s", device)

while not rospy.is_shutdown():
    ret, frame = cap.read()
    if ret:
        msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        pub.publish(msg)
    else:
        rospy.logwarn("Failed to read frame")
    rate.sleep()

cap.release()
