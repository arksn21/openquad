#!/usr/bin/env bash

cd ~/src/Firmware
source Tools/setup_gazebo.bash $(pwd) $(pwd)/build/px4_sitl_default
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools/sitl_gazebo

PS3='Please enter your choice: '
options=("Chair World" "FPV Cam World" "Optical Flow World" "Obstacle Avoidance" "Lidar World" "Vision World" "IRlock World" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Chair World")
            echo "You chose Chair World"
            # roslaunch gazebo_ros empty_world.launch world_name:=$(pwd)/Tools/sitl_gazebo/worlds/chair_world.world
            roslaunch openquad chair_world.launch
            ;;
        "FPV Cam World")
            echo "You chose FPV Cam World"
            roslaunch gazebo_ros empty_world.launch world_name:=$(pwd)/Tools/sitl_gazebo/worlds/iris_fpv_cam.world
            ;;
        "Optical Flow World")
            echo "You chose Optical Flow World"
            roslaunch gazebo_ros empty_world.launch world_name:=$(pwd)/Tools/sitl_gazebo/worlds/iris_opt_flow.world
            ;;
        "Obstacle Avoidance")
            echo "You chose Obstacle Avoidance"
            roslaunch gazebo_ros empty_world.launch world_name:=$(pwd)/Tools/sitl_gazebo/worlds/iris_obs_avoid.world
            ;;
        "Lidar World")
            echo "You chose Lidar World"
            roslaunch gazebo_ros empty_world.launch world_name:=$(pwd)/Tools/sitl_gazebo/worlds/iris_rplidar.world
            ;;
        "Vision World")
            echo "You chose Vision World"
            roslaunch gazebo_ros empty_world.launch world_name:=$(pwd)/Tools/sitl_gazebo/worlds/iris_vision.world
            ;;
        "IRlock World")
            echo "You chose IRlock World"
            roslaunch gazebo_ros empty_world.launch world_name:=$(pwd)/Tools/sitl_gazebo/worlds/iris_irlock.world
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

