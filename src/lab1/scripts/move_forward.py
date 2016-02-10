#!/usr/bin/env python
import roslib
import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Twist

def mover():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    
    recieved_warning = False
    def callback(warning):
        recieved_warning = True
    
    rospy.Subscriber("obstacle_warning", String, callback)
    
    rospy.init_node('move_forward', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        movement = Twist()
        if not recieved_warning:
            movement.linear.x = 4
        pub.publish(movement)
        rate.sleep()

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
