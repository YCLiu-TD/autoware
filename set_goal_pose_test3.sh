#!/bin/bash
source install/setup.bash
ros2 topic pub /planning/mission_planning/goal geometry_msgs/PoseStamped \
    '{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"}, pose: {position: {x: 81582.078125, y: 50124.6328125, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: -0.934849967696557, w: 0.3550430085183292}}}' \
    -1
