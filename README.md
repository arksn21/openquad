# openquad
Open Source quadcopter development platform using PX4 and ROS.<br/>
Go through the documentation process if you have any doubts.<br/>
For any queries or support email to sarthak.narayang@gmail.com<br/>
For official documentation refer this link: https://arksn21.gitbook.io/openquad/

TUTORIAL:

A two wheel drive differential bot with ultrasonic sensor.


Steps for running simulation:
1)First create two work spaces named caktin_ws and simulation_ws
2)create catkin packages inside catkin workspace:
	1)go to catkin_ws/src
	2)create catkin package with dependencies:-1)geometry_msgs, 2)rospy, 3)sensor_msgs, 4)std_msgs	and name "motion_plan"
	3)copy the python files from motion plan inside this folder to catkin_ws/src/motion_plan you have built
	4)open ternminal :1)cd ~/catkin_ws 2)catkin_make 3) source devel/setup.bash
3)create catkin packages inside simulation workspace:
	1)go to simulation_ws/src
	2)create catkin package with dependency: urdf and name "m2wr_description"
	3)copy the folder m2wr_description from simulation_ws/src inside this folder to  simulation_ws/src you have built
4) To run the simulation :
	1)open two terminals: one for gazebo and another for launch file
	2)In gazebo terminal launch world using: roslaunch gazebo_ros /*name of world*/ (For e.g. : roslaunch gazebo_ros empty_world.launch)
	3)In another teminal: 1) cd ~/simulation_ws 2) source devel/setup.bash 3) roslaunch m2wr_description spawn.launch

At this point you should have launched robot in gazebo world

To run the object detection script
1) open another terminal
2) cd ~/catkin_ws/src/motion_plan/scripts
3) chmod +x 755 *script_name*(For e.g. chmod +x 755 python.py)
4) cd ~/catin_ws
5) source devel/setup.bash
6) rosrun motion_plan *script_name*(For e.g. rosrun motion_plan object_detection.py)
