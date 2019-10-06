#!/usr/bin/env bash

roslaunch mavros px4.launch fcu_url:="udp://:14540@localhost:14557"
