#!/usr/bin/env python  

import roslib
import sys
roslib.load_manifest('subt_solution_launch')
import rospy
import geometry_msgs.msg
from nav_msgs.msg import OccupancyGrid
import tf
import time
import numpy as np
np.set_printoptions(linewidth=1000,threshold=sys.maxsize)
map_array = list(list())

def callback(data):
    global map_array
    rospy.loginfo("I heard ")
    map_array = []
    row = []
    for i in range(200):
        for j in range(200):
            row.append(data.data[(j*200) + i])
            # print(row)
        map_array.append(row)
        row = []
    map_array = np.array(map_array)
    print(map_array)



if __name__ == '__main__':
    rospy.init_node('husky_tf_listener')

    listener = tf.TransformListener()

    rate = rospy.Rate(0.2)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('X1/map', 'X1', rospy.Time(0))
            # print(trans," :  ", rot)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rospy.Subscriber("/X1/move_base/local_costmap/costmap", OccupancyGrid, callback)
        
        rate.sleep()