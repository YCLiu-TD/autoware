#!/bin/bash
source install/setup.bash
ros2 topic pub --once /planning/mission_planning/goal geometry_msgs/msg/PoseStamped '{
  "header": {
    "stamp": {
      "sec": 0,
      "nanosec": 0
    },
    "frame_id": "map"
  },
  "pose": {
    "position": {
      "x": 81589.2741351008,
      "y": 50091.69091291585,
      "z": 0.0
    },
    "orientation": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.9772988309825871,
      "w": 0.21186551149271282
    }
  }
}'
