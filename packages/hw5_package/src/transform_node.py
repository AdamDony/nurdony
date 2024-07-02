#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Vector2D
import numpy as np

# Transformation matrices
T_sensor_to_robot = np.array([
    [1, 0, -1],
    [0, 1, 0],
    [0, 0, 1]
])

T_robot_to_world = np.array([
    [-np.sqrt(2)/2, -np.sqrt(2)/2, 5 + np.sqrt(2)/2],
    [np.sqrt(2)/2, -np.sqrt(2)/2, 3 - np.sqrt(2)/2],
    [0, 0, 1]
])

T_sensor_to_world = np.dot(T_robot_to_world, T_sensor_to_robot)

def transform_callback(sensor_coord):
    point_sensor = np.array([sensor_coord.x, sensor_coord.y, 1])

    point_robot = np.dot(T_sensor_to_robot, point_sensor)
    point_world = np.dot(T_sensor_to_world, point_sensor)

    robot_coord = Vector2D(x=point_robot[0], y=point_robot[1])
    world_coord = Vector2D(x=point_world[0], y=point_world[1])

    robot_pub.publish(robot_coord)
    world_pub.publish(world_coord)

if __name__ == '__main__':
    rospy.init_node('transform_points')
    
    robot_pub = rospy.Publisher('/robot_coord', Vector2D, queue_size=10)
    world_pub = rospy.Publisher('/world_coord', Vector2D, queue_size=10)

    rospy.Subscriber('/sensor_coord', Vector2D, transform_callback)

    rospy.spin()

