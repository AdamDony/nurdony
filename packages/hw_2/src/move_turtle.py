#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_square():
    rospy.init_node('move_turtle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1) # 1 Hz

    move_cmd = Twist()
    move_cmd.linear.x = 2.0
    move_cmd.angular.z = 0.0

    for _ in range(4):
        pub.publish(move_cmd)
        rospy.sleep(2)  # Move straight for 2 seconds

        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 1.57  # 90 degrees turn
        pub.publish(move_cmd)
        rospy.sleep(2)  # Turn for 2 seconds

        move_cmd.linear.x = 2.0
        move_cmd.angular.z = 0.0

    rate.sleep()

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass

