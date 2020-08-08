#!/usr/bin/env python  
import roslib
roslib.load_manifest('subt_solution_launch')
import rospy

import tf
from nav_msgs.msg import Odometry

def transform_callback(msg, robot_name):
    br = tf.TransformBroadcaster()
    position = msg.pose.pose.position
    orn = msg.pose.pose.orientation
    br.sendTransform((position.x,position.y,position.z),
                     (orn.x,orn.y,orn.z,orn.w),
                     rospy.Time.now(),
                     robot_name,
                     robot_name+'/odom')
    print("PUBLISHED")

if __name__ == '__main__':
    # robot_name = 'X1'
    rospy.init_node('odom2robot_tf_broadcaster')
    robot_name = rospy.get_param('robot_names')
    print("GOT ROBOT NAME : ", robot_name)
    rospy.Subscriber('/'+robot_name+'/odom',
                     Odometry,
                     transform_callback,
                     robot_name)
    rospy.spin()