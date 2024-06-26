#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Vector2D
import numpy as np

def sensor_to_robot_transform(x, y):
    # Sensor is 1 meter behind the robot
    return x, y - 1

def robot_to_world_transform(x, y):
    # Robot is at (5, 3) and rotated 135 degrees relative to the x-axis
    theta = np.deg2rad(135)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    x_world = cos_theta * x - sin_theta * y + 5
    y_world = sin_theta * x + cos_theta * y + 3
    return x_world, y_world

def callback(data):
    x_sensor, y_sensor = data.x, data.y
    x_robot, y_robot = sensor_to_robot_transform(x_sensor, y_sensor)
    x_world, y_world = robot_to_world_transform(x_robot, y_robot)
    
    robot_coord = Vector2D()
    robot_coord.x = x_robot
    robot_coord.y = y_robot
    robot_pub.publish(robot_coord)
    
    world_coord = Vector2D()
    world_coord.x = x_world
    world_coord.y = y_world
    world_pub.publish(world_coord)

if __name__ == '__main__':
    rospy.init_node('coordinate_transform_node')
    robot_pub = rospy.Publisher('/robot_coord', Vector2D, queue_size=10)
    world_pub = rospy.Publisher('/world_coord', Vector2D, queue_size=10)
    rospy.Subscriber('/sensor_coord', Vector2D, callback)
    rospy.spin()

