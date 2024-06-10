#!/usr/bin/env python3
import rospy
from turtlesim_helper.msg import UnitsLabelled

def convert_distance(data):
    param = rospy.get_param('unit', 'smoots')
    distance_in_meters = data.value

    if param == 'feet':
        converted_distance = distance_in_meters * 3.28084
        unit = 'feet'
    elif param == 'smoots':
        converted_distance = distance_in_meters / 1.7018
        unit = 'smoots'
    else:
        converted_distance = distance_in_meters
        unit = 'meters'

    converted_msg = UnitsLabelled()
    converted_msg.value = converted_distance
    converted_msg.units = unit
    pub.publish(converted_msg)

if __name__ == '__main__':
    rospy.init_node('conversion_node', anonymous=True)
    rospy.Subscriber('/turtle_distance', UnitsLabelled, convert_distance)
    pub = rospy.Publisher('/converted_distance', UnitsLabelled, queue_size=10)
    rospy.spin()
