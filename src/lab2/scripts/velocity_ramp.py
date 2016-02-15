#!/usr/bin/env python
import roslib
import rospy

from geometry_msgs.msg import Twist

class VelocityRamper(object):
    """
    Class that smoothly interpolates between a raw velocity command and the
    last velocity command sent.
    """

    def __init__(self):
        rospy.init_node('velocity_ramp', anonymous=True)

        self.pub = rospy.Publisher('ramped_vel', Twist, queue_size=10)

        rospy.Subscriber("raw_vel", Twist, self.recieve_raw_velocity)
        self.last_sent = Twist()
        self.velocity_ramp_percent = rospy.get_param("/velocity_ramp_percent") / 100.0

    def recieve_raw_velocity(self, raw_velocity):
        """
        Recieve the raw velocity from another node, and publish a ramped
        velocity by interpolating between the raw velocity and the one
        published last time.
        """
        to_send = self.interpolate(self.last_sent, raw_velocity)
        self.pub.publish(to_send)
        self.last_sent = to_send

    def interpolate(self, current, goal):
        """
        Interpolate the linear x component of a Twist message between a current
        value and a goal value.
        """
        interpolated = Twist()
        interpolated.linear.x = self.lerp(current.linear.x, goal.linear.x)
        return interpolated

    def lerp(self, current, goal):
        """
        A more basic linear interpolation. Always step %3 of the difference
        between the current and the goal values.
        """

        difference = abs(current - goal)

        if difference < .001:
            #rather than endlessly interpolate small values, just move them
            #to the goal
            return goal

        if current < goal:
            return current + difference * self.velocity_ramp_percent
        else:
            return current - difference * self.velocity_ramp_percent

if __name__ == '__main__':
    try:
        ramper = VelocityRamper()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
