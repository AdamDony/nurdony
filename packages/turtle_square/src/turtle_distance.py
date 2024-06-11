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

            unit = rospy.get_param('/distance_unit', 'meters')
            converted_distance, unit_label = self.convert_distance(self.distance_traveled, unit)

            msg = UnitsLabelled()
            msg.value = converted_distance
            msg.units = unit_label
            self.publisher.publish(msg)

        self.prev_x = data.x
        self.prev_y = data.y

    def convert_distance(self, distance, unit):
        if unit == 'meters':
            return distance, 'meters'
        elif unit == 'feet':
            return distance * 3.28084, 'feet'
        elif unit == 'smoots':
            return distance / 1.7018, 'smoots'
        else:
            rospy.logwarn("Unknown unit: %s. Defaulting to meters.", unit)
            return distance, 'meters'

if __name__ == '__main__':
    rospy.init_node('turtle_distance_node')
    node = TurtleDistanceNode()
    rospy.spin()

