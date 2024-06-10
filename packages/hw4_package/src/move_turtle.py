#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time

def move_square():
    rospy.init_node('move_turtle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    move_cmd = Twist()
    
    # Define the movement command
    move_cmd.linear.x = 1.0
    move_cmd.angular.z = 0.0

    turn_cmd = Twist()
    turn_cmd.linear.x = 0.0
    turn_cmd.angular.z = 1.57  # 90 degrees in radians

    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        for _ in range(4):
            # Move forward
            pub.publish(move_cmd)
            time.sleep(2)
            
            # Stop
            move_cmd.linear.x = 0.0
            pub.publish(move_cmd)
            time.sleep(1)
            
            # Turn
            pub.publish(turn_cmd)
            time.sleep(1)
            
            # Reset move command
            move_cmd.linear.x = 1.0
            pub.publish(move_cmd)
            time.sleep(2)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass

