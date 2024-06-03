#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('turtle_square', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    move_cmd = Twist()

    while not rospy.is_shutdown():
        for _ in range(4):
            # Move forward
            move_cmd.linear.x = 2.0
            move_cmd.angular.z = 0.0
            pub.publish(move_cmd)
            rospy.sleep(2)
            # Turn
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 1.57  # 90 degrees in radians
            pub.publish(move_cmd)
            rospy.sleep(2)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass

