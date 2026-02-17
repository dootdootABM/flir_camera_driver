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

    # Get new params
    exposure_auto = LaunchConfig("exposure_auto").perform(context)
    exposure_time = float(LaunchConfig("exposure_time").perform(context))
    gain_auto = LaunchConfig("gain_auto").perform(context)
    gain = float(LaunchConfig("gain").perform(context))
    fps = float(LaunchConfig("fps").perform(context))

    if serial_arg == "auto":
        serials = get_camera_serial_numbers()
        serial = serials[0] if serials else "0"
    else:
        serial = serial_arg.strip("'\"")

    # Force Full Resolution (1440x1080) for Decimation
    cap_w = 1440
    cap_h = 1080

    if camera_type in EXAMPLE_PARAMETERS:
        camera_params = EXAMPLE_PARAMETERS[camera_type].copy()
    else:
        camera_params = EXAMPLE_PARAMETERS["firefly"].copy()

    # Apply configuration
    camera_params.update(
        {
            "image_width": cap_w,
            "image_height": cap_h,
            "offset_x": 0,
            "offset_y": 0,
            "binning_x": 1,
            "binning_y": 1,
            
            # Exposure/Gain/FPS overrides
            "exposure_auto": exposure_auto,
            "exposure_time": exposure_time,
            "gain_auto": gain_auto,
            "gain": gain,
            "frame_rate": fps,
            "frame_rate_enable": True,
            "frame_rate_auto": "Off", # We force FPS manually
        }
    )

    parameter_file_arg = LaunchConfig("parameter_file").perform(context)
    if not parameter_file_arg:
        parameter_file = PathJoinSubstitution(
            [FindPackageShare("spinnaker_camera_driver"), "config", f"{camera_type}.yaml"]
        )
    else:
        parameter_file = parameter_file_arg

    nodes = []

    # 1. Camera Driver
    nodes.append(Node(
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
    ))

    # 2. Decimator Node (720x540 Output)
    nodes.append(Node(
        package="image_proc",
        executable="crop_decimate_node",
        name="decimator",
        namespace=camera_name,
        parameters=[{
            "decimation_x": 2,
            "decimation_y": 2,
            "x_offset": 0,
            "y_offset": 0,
            "width": 0,
            "height": 0,
        }],
        remappings=[
            ("camera/image_raw", "image_raw"),
            ("camera/camera_info", "camera_info"),
            ("camera_out/image_raw", "decimated/image_raw"),
            ("camera_out/camera_info", "decimated/camera_info"),
        ],
    ))

    return nodes


def generate_launch_description():
    return LaunchDescription(
        [
            LaunchArg("camera_name", default_value="flir_camera"),
            LaunchArg("camera_type", default_value="firefly"),
            LaunchArg("serial", default_value="auto"),
            LaunchArg("parameter_file", default_value=""),
            
            # New Arguments
            LaunchArg("exposure_auto", default_value="Off", description="Exposure Auto: Off/Continuous"),
            LaunchArg("exposure_time", default_value="10000.0", description="Exposure Time (us)"),
            LaunchArg("gain_auto", default_value="Off", description="Gain Auto: Off/Continuous"),
            LaunchArg("gain", default_value="5.0", description="Gain (dB)"),
            LaunchArg("fps", default_value="60.0", description="Frame Rate (Hz)"),

            OpaqueFunction(function=launch_setup),
        ]
    )
