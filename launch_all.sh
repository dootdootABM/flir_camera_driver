#!/bin/bash

# Configuration
WORKSPACE_DIR="/home/karthik/dds_ros2/flirCAMERA/flir_camera_driver"
CAMERA_TYPE="firefly"
SERIAL="24364301"
IMAGE_WIDTH="640"
IMAGE_HEIGHT="144"

echo "---------------------------------------"
echo "Stopping existing processes..."
pkill -f "driver_node.launch.py"
pkill -f "camera_control_panel.py"
sleep 2

echo "---------------------------------------"
echo "Building package..."
cd $WORKSPACE_DIR
# Remove build artifacts
rm -rf build/ install/ log/

# Remove Python cache
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null
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
echo "Launching Camera Driver with ${IMAGE_WIDTH}x${IMAGE_HEIGHT} resolution..."
ros2 launch spinnaker_camera_driver driver_node.launch.py \
  camera_type:=$CAMERA_TYPE \
  serial:=$SERIAL \
  image_width:=$IMAGE_WIDTH \
  image_height:=$IMAGE_HEIGHT &

DRIVER_PID=$!

echo "Waiting for driver to start (5s)..."
sleep 5

echo "---------------------------------------"
echo "Launching Control Panel..."
python3 spinnaker_camera_driver/scripts/camera_control_panel.py

# Cleanup on exit
kill $DRIVER_PID
