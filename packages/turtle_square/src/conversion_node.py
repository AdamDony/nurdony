#!/usr/bin/env python3

import rospy
from turtlesim_helper.msg import UnitsLabelled

class ConversionNode:
    def __init__(self):
        self.subscriber = rospy.Subscriber('/turtle_distance', UnitsLabelled, self.callback)
        self.publisher = rospy.Publisher('/converted_distance', UnitsLabelled, queue_size=10)
        self.unit_param = rospy.get_param('/unit', 'smoots')

    def callback(self, data):
        converted_msg = UnitsLabelled()
        converted_msg.value = data.value
        if self.unit_param == 'feet':
            converted_msg.value = data.value * 3.28084  # convert meters to feet
            converted_msg.units = 'feet'
        elif self.unit_param == 'smoots':
            converted_msg.value = data.value / 1.7018  # convert meters to smoots
            converted_msg.units = 'smoots'
        else:
            converted_msg.units = 'meters'
        self.publisher.publish(converted_msg)

if __name__ == '__main__':
    rospy.init_node('conversion_node')
    node = ConversionNode()
    rospy.spin()
