#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from turtlesim_helper.msg import UnitsLabelled
import math

class TurtleDistanceNode:
    def __init__(self):
        self.subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.publisher = rospy.Publisher('/turtle_distance', UnitsLabelled, queue_size=10)
        self.prev_x = None
        self.prev_y = None
        self.distance_traveled = 0.0

    def pose_callback(self, data):
        if self.prev_x is not None and self.prev_y is not None:
            distance = math.sqrt((data.x - self.prev_x)**2 + (data.y - self.prev_y)**2)
            self.distance_traveled += distance

            msg = UnitsLabelled()
            msg.value = self.distance_traveled
            msg.units = "meters"
            self.publisher.publish(msg)

        self.prev_x = data.x
        self.prev_y = data.y

if __name__ == '__main__':
    rospy.init_node('turtle_distance_node')
    node = TurtleDistanceNode()
    rospy.spin()

