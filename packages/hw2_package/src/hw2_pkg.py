#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_square():
    rospy.init_node('move_turtle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    vel_msg = Twist()

    while not rospy.is_shutdown():
        for _ in range(4):
            vel_msg.linear.x = 2.0
            vel_msg.angular.z = 0.0
            velocity_publisher.publish(vel_msg)
            rospy.sleep(2)

            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 1.57
            velocity_publisher.publish(vel_msg)
            rospy.sleep(2)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass

