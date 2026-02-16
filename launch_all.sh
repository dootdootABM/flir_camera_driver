#!/bin/bash

# Configuration
WORKSPACE_DIR="/home/karthik/dds_ros2/flirCAMERA/flir_camera_driver"
CAMERA_TYPE="firefly"
SERIAL="24364301"

echo "---------------------------------------"
echo "Stopping existing processes..."
pkill -f "driver_node.launch.py"
pkill -f "camera_control_panel.py"
sleep 2

echo "---------------------------------------"
echo "Building package..."
cd $WORKSPACE_DIR
colcon build --symlink-install --packages-up-to spinnaker_camera_driver

if [ $? -ne 0 ]; then
    echo "Build failed! Exiting."
    exit 1
fi

echo "---------------------------------------"
echo "Sourcing workspace..."
source /opt/ros/humble/setup.bash
source install/setup.bash

echo "---------------------------------------"
echo "Launching Camera Driver..."
ros2 launch spinnaker_camera_driver driver_node.launch.py camera_type:=$CAMERA_TYPE serial:=$SERIAL &
DRIVER_PID=$!

echo "Waiting for driver to start (5s)..."
sleep 5

echo "---------------------------------------"
echo "Launching Control Panel..."
python3 spinnaker_camera_driver/scripts/camera_control_panel.py

# Cleanup on exit
kill $DRIVER_PID
