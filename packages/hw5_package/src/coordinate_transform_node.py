#!/usr/bin/env python3
import rospy
from hw5_package.msg import Vector2D
import math

def sensor_to_robot(x, y):
    x_r = x + 1  # sensor is 1 meter behind robot center
    y_r = y
    return x_r, y_r

def robot_to_world(x, y, theta, x_w, y_w):
    x_w_new = x_w + (x * math.cos(theta) - y * math.sin(theta))
    y_w_new = y_w + (x * math.sin(theta) + y * math.cos(theta))
    return x_w_new, y_w_new

def callback(data):
    sensor_x = data.x
    sensor_y = data.y
    robot_x = 5
    robot_y = 3
    robot_theta = math.radians(135)
    robot_x_r, robot_y_r = sensor_to_robot(sensor_x, sensor_y)
    world_x, world_y = robot_to_world(robot_x_r, robot_y_r, robot_theta, robot_x, robot_y)
    robot_coord = Vector2D()
    robot_coord.x = robot_x_r
    robot_coord.y = robot_y_r
    robot_coord_pub.publish(robot_coord)
    world_coord = Vector2D()
    world_coord.x = world_x
    world_coord.y = world_y
    world_coord_pub.publish(world_coord)

def coordinate_transform_node():
    rospy.init_node('coordinate_transform_node', anonymous=True)
    rospy.Subscriber('/sensor_coord', Vector2D, callback)
    global robot_coord_pub, world_coord_pub
    robot_coord_pub = rospy.Publisher('/robot_coord', Vector2D, queue_size=10)
    world_coord_pub = rospy.Publisher('/world_coord', Vector2D, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        coordinate_transform_node()
    except rospy.ROSInterruptException:
        pass
