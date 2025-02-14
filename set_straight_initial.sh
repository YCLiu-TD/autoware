#!/bin/bash
source ../install/setup.bash

ros2 topic pub --once /initialpose geometry_msgs/msg/PoseWithCovarianceStamped '{
  "header": {
    "stamp": {
      "sec": 1739360906,
      "nanosec": 403231800
    },
    "frame_id": "map"
  },
  "pose": {
    "pose": {
      "position": {
        "x": 81580.171875,
        "y": 50095.83203125,
        "z": 0.0
      },
      "orientation": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.9772988309825871,
        "w": 0.21186551149271282
      }
    },
    "covariance": [
      0.25, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.25, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891909122467
    ]
  }
}'
