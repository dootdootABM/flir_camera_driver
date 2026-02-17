#!/usr/bin/env python3

import os
import re

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument as LaunchArg
from launch.actions import OpaqueFunction
from launch.substitutions import LaunchConfiguration as LaunchConfig
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def get_camera_serial_numbers():
    serials = []
    try:
        if os.path.exists("/dev/v4l/by-id"):
            for name in os.listdir("/dev/v4l/by-id"):
                if ("FLIR" in name) or ("Firefly" in name) or ("Blackfly" in name):
                    m = re.search(r"[-_](\d{7,9})[-_]", name)
                    if m:
                        s = m.group(1)
                        if s not in serials:
                            serials.append(s)
    except Exception:
        pass
    return serials


EXAMPLE_PARAMETERS = {
    "firefly": {
        "debug": False,
        "compute_brightness": False,
        "dump_node_map": False,
        "exposure_auto": "Off",
        "exposure_time": 10000.0,
        "gain_auto": "Off",
        "gain": 5.0,
        "frame_rate_auto": "Off",
        "frame_rate": 60.0,
        "frame_rate_enable": True,
        "trigger_mode": "Off",
        "chunk_mode_active": True,
        "chunk_enable_frame_id": True,
        "balance_white_auto": "Continuous",
    },
    "blackfly_s": {"exposure_auto": "Off", "balance_white_auto": "Continuous"},
    "blackfly": {"exposure_auto": "Off", "balance_white_auto": "Continuous"},
}


def launch_setup(context, *args, **kwargs):
    camera_type = LaunchConfig("camera_type").perform(context)
    serial_arg = LaunchConfig("serial").perform(context)
    camera_name = LaunchConfig("camera_name").perform(context)

    if serial_arg == "auto":
        serials = get_camera_serial_numbers()
        serial = serials[0] if serials else "0"
    else:
        serial = serial_arg.strip("'\"")

    # Force 640x480 Center Crop
    # Full sensor is 1440x1080 (Firefly)
    # Target: 640x480
    # Offset X = (1440 - 640) / 2 = 400
    # Offset Y = (1080 - 480) / 2 = 300
    
    cap_w = 640
    cap_h = 480
    off_x = 400
    off_y = 300

    if camera_type in EXAMPLE_PARAMETERS:
        camera_params = EXAMPLE_PARAMETERS[camera_type].copy()
    else:
        camera_params = EXAMPLE_PARAMETERS["firefly"].copy()

    camera_params.update(
        {
            "image_width": cap_w,
            "image_height": cap_h,
            "offset_x": off_x,
            "offset_y": off_y,
            "binning_x": 1,
            "binning_y": 1,
        }
    )

    parameter_file_arg = LaunchConfig("parameter_file").perform(context)
    if not parameter_file_arg:
        parameter_file = PathJoinSubstitution(
            [FindPackageShare("spinnaker_camera_driver"), "config", f"{camera_type}.yaml"]
        )
    else:
        parameter_file = parameter_file_arg

    nodes = [
        Node(
            package="spinnaker_camera_driver",
            executable="camera_driver_node",
            output="screen",
            name=camera_name,
            parameters=[
                camera_params,
                {
                    "parameter_file": parameter_file,
                    "serial_number": serial,
                    "ffmpeg_image_transport.encoding": "hevc_nvenc",
                },
            ],
            remappings=[
                ("~/control", "/exposure_control/control"),
            ],
        )
    ]

    return nodes


def generate_launch_description():
    return LaunchDescription(
        [
            LaunchArg("camera_name", default_value="flir_camera"),
            LaunchArg("camera_type", default_value="firefly"),
            LaunchArg("serial", default_value="auto"),
            LaunchArg("parameter_file", default_value=""),
            # Width/Height args are ignored here as we hardcoded center crop
            OpaqueFunction(function=launch_setup),
        ]
    )
