Lab 1
=====

This code is a simple robot simulation that moves a robot forward until an
obstacle is detected. The obstacle is detected by a simulated laser scan, which
goes from 135 degrees left of robot forward center to 135 degrees right of robot
'warning_distance' inside `lab1_stop_at_obstacle.launch`.

The code is organized as two ROS nodes, one which detects obstacles using the
laser scan (obstacle_warning.py), and one which moves the robot until an
obstacle is signaled by the other node (move_forward.py).

The demonstration can be run with `roslaunch lab1_stop_at_obstacle.launch`.

Math for conversion between polar and Cartesian coordinates was taken from
https://www.mathsisfun.com/polar-cartesian-coordinates.html.

Some source code was taken from the ROS tutorials on writing simple publishers
and subscribers and modified.
http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
