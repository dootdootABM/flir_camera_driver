#!/bin/bash

# Configuration
WORKSPACE_DIR="/home/karthik/dds_ros2/flirCAMERA/flir_camera_driver"
CAMERA_TYPE="firefly"
SERIAL="24364301"

# --- Camera Parameters ---
# Exposure: "Off" (Manual) or "Continuous" (Auto)
EXPOSURE_AUTO="Off"
# Exposure Time (us) - ignored if Auto
EXPOSURE_TIME="5000.0"

# Gain: "Off" (Manual) or "Continuous" (Auto)
GAIN_AUTO="Off"
# Gain (dB) - ignored if Auto
GAIN="30"

# Frame Rate (Hz)
FPS="60.0"


# --- 1. Clean & Rebuild ---
echo "---------------------------------------"
echo "Stopping existing processes..."
pkill -f "driver_node.launch.py"
pkill -f "camera_driver_node"
sleep 1

echo "---------------------------------------"
echo "Rebuilding..."
cd "$WORKSPACE_DIR" || exit 1
# Keeping it fast:
colcon build --packages-select spinnaker_camera_driver

echo "---------------------------------------"
echo "Sourcing..."
source /opt/ros/humble/setup.bash
source install/setup.bash

# --- 2. Launch ---
echo "---------------------------------------"
echo "Launching Camera Driver with Decimation..."
echo "  Exposure: $EXPOSURE_AUTO / $EXPOSURE_TIME us"
echo "  Gain:     $GAIN_AUTO / $GAIN dB"
echo "  FPS:      $FPS Hz"

ros2 launch spinnaker_camera_driver driver_node.launch.py \
  camera_type:=$CAMERA_TYPE \
  serial:=$SERIAL \
  exposure_auto:=$EXPOSURE_AUTO \
  exposure_time:=$EXPOSURE_TIME \
  gain_auto:=$GAIN_AUTO \
  gain:=$GAIN \
  fps:=$FPS &

PID=$!
echo "Driver running (PID: $PID). View with:"
echo "  ros2 run image_tools showimage --ros-args -r image:=/flir_camera/decimated/image_raw"
wait $PID
