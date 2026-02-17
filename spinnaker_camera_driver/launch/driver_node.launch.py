#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright 2022 Bernd Pfrommer
# Licensed under the Apache License, Version 2.0
# -----------------------------------------------------------------------------

import os
import re

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument as LaunchArg
from launch.actions import OpaqueFunction
from launch.substitutions import LaunchConfiguration as LaunchConfig
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


CAMERA_MAX_RESOLUTIONS = {
    "firefly": {"width": 1440, "height": 1080},
    "blackfly_s": {"width": 2448, "height": 2048},
    "blackfly": {"width": 1920, "height": 1200},
}


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

    if not serials:
        try:
            import subprocess
            result = subprocess.run(
                ["v4l2-ctl", "--list-devices"],
                capture_output=True,
                text=True,
                timeout=2,
            )
            for line in result.stdout.split("\n"):
                if ("FLIR" in line) or ("Firefly" in line):
                    m = re.search(r"(\d{7,9})", line)
                    if m:
                        serials.append(m.group(1))
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
    },
    "blackfly_s": {
        "exposure_auto": "Off",
    },
    "blackfly": {
        "exposure_auto": "Off",
    },
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

    if camera_type in CAMERA_MAX_RESOLUTIONS:
        max_w = CAMERA_MAX_RESOLUTIONS[camera_type]["width"]
        max_h = CAMERA_MAX_RESOLUTIONS[camera_type]["height"]
    else:
        max_w, max_h = 1440, 1080

    target_w = int(LaunchConfig("image_width").perform(context))
    target_h = int(LaunchConfig("image_height").perform(context))

    if camera_type in EXAMPLE_PARAMETERS:
        camera_params = EXAMPLE_PARAMETERS[camera_type].copy()
    else:
        camera_params = EXAMPLE_PARAMETERS["firefly"].copy()

    camera_params.update(
        {
            "image_width": max_w,
            "image_height": max_h,
            "offset_x": 0,
            "offset_y": 0,
            "binning_x": 1,
            "binning_y": 1,
            "serial_number": serial,
            "parameter_file": PathJoinSubstitution(
                [FindPackageShare("spinnaker_camera_driver"), "config", f"{camera_type}.yaml"]
            ),
        }
    )

    nodes = []

    nodes.append(
        Node(
            package="spinnaker_camera_driver",
            executable="camera_driver_node",
            output="screen",
            name=camera_name,
            parameters=[camera_params],
            remappings=[
                ("~/control", "/exposure_control/control"),
            ],
        )
    )

    nodes.append(
        Node(
            package="image_proc",
            executable="resize_node",
            name="image_resizer",
            namespace=camera_name,
            parameters=[
                {
                    "use_scale": False,
                    "width": target_w,
                    "height": target_h,
                    "interpolation": 1,
                }
            ],
            remappings=[
                ("image/image_raw", "image_raw"),
                ("image/camera_info", "camera_info"),
                ("resize/image_raw", "image_resized"),
                ("resize/camera_info", "camera_info_resized"),
            ],
            arguments=[
                "--ros-args",
                "--param", "qos_overrides./image.subscription.reliability:=best_effort",
                "--param", "qos_overrides./camera_info.subscription.reliability:=best_effort",
            ],
        )
    )

    return nodes


def generate_launch_description():
    return LaunchDescription(
        [
            LaunchArg("camera_name", default_value="flir_camera"),
            LaunchArg("camera_type", default_value="firefly"),
            LaunchArg("serial", default_value="auto"),
            LaunchArg("image_width", default_value="1440", description="Target Width"),
            LaunchArg("image_height", default_value="1080", description="Target Height"),
            OpaqueFunction(function=launch_setup),
        ]
    )
