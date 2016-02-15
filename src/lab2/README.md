# Lab 2

This code moves a robot forward until an obstacle is detected. The obstacle is
detected by a Kinect depth scan, transformed to a 'laser scan', which goes from
30 degrees left of robot forward center to 30 degrees right of robot.

The distance at which the robot will stop is set inside `lab2_pc.launch` with
"warning_distance_length_cm". In addition, the robot leaves enough width for it
to fit through narrow passages set with "warning_distance_width_cm".

The code is organized as three ROS nodes, one which detects obstacles using the
laser scan (obstacle_warning.py), one which moves the robot until an obstacle is
signaled by the other node (move_forward.py), and one which smoothly ramps
velocities up and down (velocity_ramp).

### Running the Simulation

The demonstration can be run with `roslaunch lab2_turtle.launch` on the
Turtlebot, and `roslaunch lab2_pc.launch` on the computer.

### References
+ Math for [conversion between polar and Cartesian coordinates] (https://www.mathsisfun.com/polar-cartesian-coordinates.html).

+ Some source code was taken from the [ROS tutorials on writing simple publishers and subscribers] (http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29) and modified.
