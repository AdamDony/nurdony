#!/usr/bin/env python3

import rospy

class ParamSetterNode:
    def __init__(self):
        self.rate = rospy.Rate(0.2)  # 5 seconds
        self.units = ['meters', 'feet', 'smoots']
        self.index = 0

    def run(self):
        while not rospy.is_shutdown():
            rospy.set_param('/unit', self.units[self.index])
            self.index = (self.index + 1) % len(self.units)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('param_setter_node')
    node = ParamSetterNode()
    node.run()
