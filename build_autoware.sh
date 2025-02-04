#!/bin/bash

colcon build \
    --cmake-args \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
    -DCMAKE_C_COMPILER_LAUNCHER=ccache -DCMAKE_CXX_COMPILER_LAUNCHER=ccache \
    --symlink-install

# -DCMAKE_BUILD_TYPE=RelWithDebInfo \
