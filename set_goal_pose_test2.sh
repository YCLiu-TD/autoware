#!/bin/bash
source install/setup.bash
ros2 topic pub /planning/mission_planning/goal geometry_msgs/PoseStamped \
    '{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"}, pose: {position: {x: 81587.671875, y: 50093.94140625, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: -0.9957377945723164, w: 0.09222930369605731}}}' \
    -1
