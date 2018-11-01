#!/usr/bin/env python

import sys
sys.path.insert(0, '/home/alexandre/catkin_ws/src/ros_mitsubishi/src')

import RobotArm
robot = RobotArm.RobotArm()

import rospy
from ros_mitsubishi.msg import CartesianMessage

def callback(data):
    rospy.loginfo(" I heard %s", data)
    
    robot.init()
    robot.moveCartesianPosition(data.x, data.y, data.z, data.a, data.b, data.speed) #x, y, z, a, b, speed
    robot.reset()

    
def listener():
    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber("cartesianMovement", CartesianMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()