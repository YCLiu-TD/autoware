#!/bin/bash
source install/setup.bash
ros2 topic pub /planning/mission_planning/goal geometry_msgs/PoseStamped \
    '{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"}, pose: {position: {x: 81571.125, y: 50091.2890625, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0701835685155175, w: 0.9975340930065637}}}' \
    -1
