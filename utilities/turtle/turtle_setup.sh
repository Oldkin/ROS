source ../venv/bin/activate    #activate the virtualenv

#upload the ip address to thewrong.info
python turtle_setup.py

deactivate #deactivate the virtualenv

#set the environment for the master node to run
export ROS_MASTER_URI=http://localhost:11311/
source turtle_ip.sh #contains export for ROS_HOSTNAME

export TURTLEBOT_3D_SENSOR=kinect
