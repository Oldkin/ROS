#!/usr/bin/env python
import math

import roslib
import rospy

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan



class LaserCallback(object):

    def __init__(self, warning_publisher):
        self.warning_publisher = warning_publisher
        self.warning_box = {
            "width":rospy.get_param("/warning_distance_width_cm")/2,
            "length":rospy.get_param("/warning_distance_length_cm"),
        }

    def callback(self, scan):
        start_angle = scan.angle_min
        increment = scan.angle_increment

        #convert to cartesian coordinates
        #taken from https://www.mathsisfun.com/polar-cartesian-coordinates.html
        for hit_index, hit_radius in enumerate(scan.ranges):
            if math.isnan(hit_radius):
                continue
            if hit_radius >= scan.range_max or hit_radius <= scan.range_min:
                continue

            radius_in_cm = hit_radius * 100

            angle = hit_index * increment + start_angle
            x = radius_in_cm * math.sin(angle)
            y = radius_in_cm * math.cos(angle)

            if self.check_box(x, y):
                self.warning_publisher.publish("obstacle! YIKES!")

    def check_box(self, x, y):
        x_hit = -self.warning_box["width"] < x < self.warning_box["width"]
        y_hit = y < self.warning_box["length"]
        return x_hit and y_hit

if __name__ == "__main__":
    rospy.init_node("obstacle_warning", anonymous=True)

    pub = rospy.Publisher('obstacle_warning', String, queue_size=10)

    laser_callback = LaserCallback(pub)

    rospy.Subscriber("base_scan", LaserScan, laser_callback.callback)

    rospy.spin()
