#!/bin/bash
source ../install/setup.bash

ros2 topic pub --once /initialpose geometry_msgs/msg/PoseWithCovarianceStamped '{
  "header": {
    "stamp": {
      "sec": 1739256805,
      "nanosec": 587954677
    },
    "frame_id": "map"
  },
  "pose": {
    "pose": {
      "position": {
        "x": 81580.609375,
        "y": 50084.8046875,
        "z": 0.0
      },
      "orientation": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.7625865842394736,
        "w": 0.6468861580973675
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
