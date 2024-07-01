#!/usr/bin/env python3
import rospy
import math
from duckietown_msgs.msg import Vector2D

class TransformNode:
    def __init__(self):
        self.sensor_to_robot = [1, 0]
        self.robot_to_world_rotation = [[-math.sqrt(2)/2, -math.sqrt(2)/2], 
                                        [math.sqrt(2)/2, -math.sqrt(2)/2]]
        self.robot_to_world_translation = [5, 3]

        rospy.Subscriber('/sensor_coord', Vector2D, self.transform_callback)
        self.robot_coord_pub = rospy.Publisher('/robot_coord', Vector2D, queue_size=10)
        self.world_coord_pub = rospy.Publisher('/world_coord', Vector2D, queue_size=10)

    def transform_callback(self, msg):
        sensor_x, sensor_y = msg.x, msg.y

        # Transform to robot frame
        robot_x = sensor_x + self.sensor_to_robot[0]
        robot_y = sensor_y + self.sensor_to_robot[1]
        robot_coord = Vector2D()
        robot_coord.x, robot_coord.y = robot_x, robot_y
        self.robot_coord_pub.publish(robot_coord)

        # Transform to world frame
        world_x = (self.robot_to_world_rotation[0][0] * robot_x + 
                   self.robot_to_world_rotation[0][1] * robot_y + 
                   self.robot_to_world_translation[0])
        world_y = (self.robot_to_world_rotation[1][0] * robot_x + 
                   self.robot_to_world_rotation[1][1] * robot_y + 
                   self.robot_to_world_translation[1])
        world_coord = Vector2D()
        world_coord.x, world_coord.y = world_x, world_y
        self.world_coord_pub.publish(world_coord)

if __name__ == '__main__':
    rospy.init_node('transform_node', anonymous=True)
    node = TransformNode()
    rospy.spin()
