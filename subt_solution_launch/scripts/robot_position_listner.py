#!/usr/bin/env python  

import roslib
roslib.load_manifest('subt_solution_launch')
import rospy
import geometry_msgs.msg
import tf
import time

if __name__ == '__main__':
    rospy.init_node('husky_tf_listener')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('X1/map', 'X1', rospy.Time(0))
            print(trans," :  ", rot)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        time.sleep(1)