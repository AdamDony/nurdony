#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('move_turtle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    vel_msg = Twist()

    while not rospy.is_shutdown():
        # Move forward
        vel_msg.linear.x = 2.0
        vel_msg.angular.z = 0.0
        for _ in range(4):
            velocity_publisher.publish(vel_msg)
            rate.sleep()

        # Turn 90 degrees
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 1.57  # 90 degrees in radians
        for _ in range(2):
            velocity_publisher.publish(vel_msg)
            rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
