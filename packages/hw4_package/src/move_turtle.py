#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('move_turtle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz
    
    while not rospy.is_shutdown():
        move_cmd = Twist()
        move_cmd.linear.x = 1.0
        move_cmd.angular.z = 1.0
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
