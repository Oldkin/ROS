#!/usr/bin/env python
import roslib
import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Twist

class MoveForward(object):
    
    def __init__(self):
        rospy.init_node('move_forward', anonymous=True)
    
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        
        self.obstacle_warning = False
        rospy.Subscriber("obstacle_warning", String, self.recieve_warning)
        
    def recieve_warning(self, warning):
        self.obstacle_warning = True
        
    def spin(self):
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            movement = Twist()
            if not self.obstacle_warning:
                movement.linear.x = 1
            self.pub.publish(movement)
            rate.sleep()
            
if __name__ == '__main__':
    try:
        mover = MoveForward()
        mover.spin()
    except rospy.ROSInterruptException:
        pass
