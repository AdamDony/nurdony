#!/usr/bin/env python3
import rospy
import time

def set_param():
    rospy.set_param('unit', 'meters')
    rospy.loginfo("Set param to meters")
    time.sleep(5)
    rospy.set_param('unit', 'feet')
    rospy.loginfo("Set param to feet")
    time.sleep(5)
    rospy.set_param('unit', 'smoots')
    rospy.loginfo("Set param to smoots")
    time.sleep(5)

if __name__ == '__main__':
    rospy.init_node('param_setter_node', anonymous=True)
    while not rospy.is_shutdown():
        set_param()

