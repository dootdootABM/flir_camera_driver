#!/bin/bash

# Configuration
WORKSPACE_DIR="/home/karthik/dds_ros2/flirCAMERA/flir_camera_driver"
CAMERA_TYPE="firefly"
SERIAL="24364301"

# --- 1. Clean & Rebuild ---
echo "---------------------------------------"
echo "Stopping existing processes..."
pkill -f "driver_node.launch.py"
pkill -f "camera_driver_node"
sleep 2

echo "---------------------------------------"
echo "Wiping build artifacts..."
cd "$WORKSPACE_DIR" || exit 1
rm -rf build/ install/ log/

echo "---------------------------------------"
echo "Building package..."
# Build only the driver package to save time
colcon build --packages-select spinnaker_camera_driver

if [ $? -ne 0 ]; then
    echo "Build failed! Exiting."
    exit 1
fi

echo "---------------------------------------"
echo "Sourcing workspace..."
source /opt/ros/humble/setup.bash
source install/setup.bash

# --- 2. Launch ---
echo "---------------------------------------"
echo "Launching Camera Driver..."
# Note: image_width/height are now ignored by the launch file
# because it forces full res + decimation for max performance.
ros2 launch spinnaker_camera_driver driver_node.launch.py \
  camera_type:=$CAMERA_TYPE \
  serial:=$SERIAL &

DRIVER_PID=$!

echo "---------------------------------------"
echo "Driver running with PID: $DRIVER_PID"
echo "Monitor topic rate with: ros2 topic hz /flir_camera/image_raw"
echo "Monitor resolution with: ros2 topic echo --once /flir_camera/image_raw | grep -E 'width|height'"
echo "Press Ctrl+C to stop."

# Wait for user interrupt
wait $DRIVER_PID
