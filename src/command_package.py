#!/usr/bin/env python

import mavros
from mavros import command

mavros.set_namespace()

# arming
command.arming(True)

# takeoff
command.takeoff(altitude = 5, latitude = 0, longitude = 0, min_pitch = 0, yaw = 0)

# disarming
command.arming(False)