#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_square():
    rospy.init_node('turtle_square_node', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    move_cmd = Twist()
    move_cmd.linear.x = 2.0
    move_cmd.angular.z = 0.0

    turn_cmd = Twist()
    turn_cmd.linear.x = 0.0
    turn_cmd.angular.z = 1.57  # 90 degrees in radians

    for _ in range(4):
        for _ in range(4):  # Move straight
            pub.publish(move_cmd)
            rate.sleep()
        for _ in range(2):  # Turn
            pub.publish(turn_cmd)
            rate.sleep()

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass

