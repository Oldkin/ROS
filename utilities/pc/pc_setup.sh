source ../venv/bin/activate    #activate the virtualenv

#download the ip address to thewrong.info
python pc_setup.py

deactivate #deactivate the virtualenv

#set the environment for the master node to run
source pc_ip.sh #contains export for ROS_HOSTNAME and ROS_MASTER_URI
