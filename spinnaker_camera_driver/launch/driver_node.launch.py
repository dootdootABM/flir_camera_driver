# -----------------------------------------------------------------------------
# Copyright 2022 Bernd Pfrommer <bernd.pfrommer@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument as LaunchArg
from launch.actions import OpaqueFunction
from launch.substitutions import LaunchConfiguration as LaunchConfig
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import subprocess
import re

# Camera native resolutions
CAMERA_MAX_RESOLUTIONS = {
    'blackfly_s': {'width': 2448, 'height': 2048},
    'blackfly': {'width': 1920, 'height': 1200},
    'chameleon': {'width': 2048, 'height': 1536},
    'grasshopper': {'width': 2448, 'height': 2048},
    'firefly': {'width': 1440, 'height': 1080},
    'flir_ax5': {'width': 640, 'height': 512},
}

def get_camera_serial_numbers():
    """
    Auto-detect connected FLIR camera serial numbers.
    Returns list of serial numbers.
    """
    try:
        # Try using SpinView CLI tools if available
        result = subprocess.run(
            ['spinview-cli', '--list'],
            capture_output=True,
            text=True,
            timeout=5
        )
        serials = re.findall(r'Serial:\s*(\d+)', result.stdout)
        return serials
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    try:
        # Alternative: use v4l2 for USB cameras
        result = subprocess.run(
            ['v4l2-ctl', '--list-devices'],
            capture_output=True,
            text=True,
            timeout=5
        )
        # Extract FLIR camera info
        serials = []
        lines = result.stdout.split('\n')
        for i, line in enumerate(lines):
            if 'FLIR' in line or 'Blackfly' in line or 'Chameleon' in line or 'Grasshopper' in line:
                serial_match = re.search(r'(\d{8,})', line)
                if serial_match:
                    serials.append(serial_match.group(1))
        return serials
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    return []

def calculate_binning(max_res, desired_res):
    """
    Calculate binning values based on desired resolution.
    Returns binning_x, binning_y, and actual output resolution.
    """
    binning_x = max(1, round(max_res['width'] / desired_res['width']))
    binning_y = max(1, round(max_res['height'] / desired_res['height']))
    
    # Calculate actual output resolution after binning
    actual_width = max_res['width'] // binning_x
    actual_height = max_res['height'] // binning_y
    
    return binning_x, binning_y, actual_width, actual_height

example_parameters = {
    'blackfly_s': {
        'debug': False,
        'compute_brightness': False,
        'adjust_timestamp': True,
        'dump_node_map': False,
        # Exposure settings
        'exposure_auto': 'Off',
        'exposure_time': 10000.0,
        # Gain settings
        'gain_auto': 'Off',
        'gain': 5.0,
        # Frame rate
        'frame_rate_auto': 'Off',
        'frame_rate': 40.0,
        'frame_rate_enable': True,
        'buffer_queue_size': 10,
        'trigger_mode': 'Off',
        'chunk_mode_active': True,
        'chunk_selector_frame_id': 'FrameID',
        'chunk_enable_frame_id': True,
        'chunk_selector_exposure_time': 'ExposureTime',
        'chunk_enable_exposure_time': True,
        'chunk_selector_gain': 'Gain',
        'chunk_enable_gain': True,
        'chunk_selector_timestamp': 'Timestamp',
        'chunk_enable_timestamp': True,
        'diagnostic_period': 1.0,
        'diagnostic_min_freq': 39.0,
        'diagnostic_max_freq': 41.0
    },
    'blackfly': {
        'debug': False,
        'dump_node_map': False,
        'gain_auto': 'Continuous',
        'pixel_format': 'BayerRG8',
        'exposure_auto': 'Continuous',
        'frame_rate_auto': 'Off',
        'frame_rate': 40.0,
        'frame_rate_enable': True,
        'buffer_queue_size': 10,
        'trigger_mode': 'Off',
    },
    'chameleon': {
        'debug': False,
        'compute_brightness': False,
        'dump_node_map': False,
        'gain_auto': 'Continuous',
        'exposure_auto': 'Continuous',
        'offset_x': 0,
        'offset_y': 0,
        'pixel_format': 'RGB8',
        'frame_rate_continous': True,
        'frame_rate': 100.0,
        'trigger_mode': 'Off',
        'chunk_mode_active': True,
        'chunk_selector_frame_id': 'FrameID',
        'chunk_enable_frame_id': True,
        'chunk_selector_exposure_time': 'ExposureTime',
        'chunk_enable_exposure_time': True,
        'chunk_selector_gain': 'Gain',
        'chunk_enable_gain': True,
        'chunk_selector_timestamp': 'Timestamp',
        'chunk_enable_timestamp': True,
    },
    'grasshopper': {
        'debug': False,
        'compute_brightness': False,
        'dump_node_map': False,
        'gain_auto': 'Continuous',
        'exposure_auto': 'Continuous',
        'frame_rate_auto': 'Off',
        'frame_rate': 100.0,
        'trigger_mode': 'Off',
        'chunk_mode_active': True,
        'chunk_selector_frame_id': 'FrameID',
        'chunk_enable_frame_id': True,
        'chunk_selector_exposure_time': 'ExposureTime',
        'chunk_enable_exposure_time': True,
        'chunk_selector_gain': 'Gain',
        'chunk_enable_gain': True,
        'chunk_selector_timestamp': 'Timestamp',
        'chunk_enable_timestamp': True,
    },
    'firefly': {
        'debug': False,
        'compute_brightness': False,
        'dump_node_map': False,
        'gain_auto': 'Continuous',
        'exposure_auto': 'Continuous',
        'frame_rate_auto': 'Off',
        'frame_rate': 60.0,
        'frame_rate_enable': True,
        'trigger_mode': 'Off',
        'chunk_mode_active': True,
        'chunk_selector_frame_id': 'FrameID',
        'chunk_enable_frame_id': True,
        'chunk_selector_exposure_time': 'ExposureTime',
        'chunk_enable_exposure_time': True,
        'chunk_selector_gain': 'Gain',
        'chunk_enable_gain': True,
        'chunk_selector_timestamp': 'Timestamp',
        'chunk_enable_timestamp': True,
    },
    'flir_ax5': {
        'debug': False,
        'compute_brightness': False,
        'adjust_timestamp': False,
        'dump_node_map': False,
        'pixel_format': 'Mono8',
        'gev_scps_packet_size': 576,
        'offset_x': 0,
        'offset_y': 0,
        'sensor_gain_mode': 'HighGainMode',
        'nuc_mode': 'Automatic',
        'sensor_dde_mode': 'Automatic',
        'sensor_video_standard': 'NTSC30HZ',
        'image_adjust_method': 'PlateauHistogram',
        'video_orientation': 'Normal',
    },
}


def launch_setup(context, *args, **kwargs):
    """Launch camera driver node."""
    parameter_file = LaunchConfig('parameter_file').perform(context)
    camera_type = LaunchConfig('camera_type').perform(context)
    serial_arg = LaunchConfig('serial').perform(context)
    
    # Auto-detect serial if set to 'auto'
    if serial_arg == 'auto':
        detected_serials = get_camera_serial_numbers()
        if not detected_serials:
            raise Exception('Auto-detection enabled but no FLIR cameras found!')
        serial = detected_serials[0]
        print(f"Auto-detected camera serial numbers: {detected_serials}")
        print(f"Using serial: {serial}")
    else:
        serial = serial_arg.strip("'\"")
    
    # Get desired resolution from launch arguments
    desired_width = int(LaunchConfig('image_width').perform(context))
    desired_height = int(LaunchConfig('image_height').perform(context))
    
    if not parameter_file:
        parameter_file = PathJoinSubstitution(
            [FindPackageShare('spinnaker_camera_driver'), 'config', camera_type + '.yaml']
        )
    if camera_type not in example_parameters:
        raise Exception('no example parameters available for type ' + camera_type)
    
    if camera_type not in CAMERA_MAX_RESOLUTIONS:
        raise Exception('no max resolution defined for camera type ' + camera_type)
    
    # Calculate binning and actual resolution
    max_res = CAMERA_MAX_RESOLUTIONS[camera_type]
    binning_x, binning_y, actual_width, actual_height = calculate_binning(
        max_res, {'width': desired_width, 'height': desired_height}
    )
    
    print(f"Camera: {camera_type}")
    print(f"Serial: {serial}")
    print(f"Native resolution: {max_res['width']}x{max_res['height']}")
    print(f"Desired resolution: {desired_width}x{desired_height}")
    print(f"Calculated binning: {binning_x}x{binning_y}")
    print(f"Actual output resolution: {actual_width}x{actual_height}")
    
    # Add binning and resolution parameters
    camera_params = example_parameters[camera_type].copy()
    camera_params['binning_x'] = binning_x
    camera_params['binning_y'] = binning_y
    camera_params['image_width'] = actual_width
    camera_params['image_height'] = actual_height
    camera_params['offset_x'] = 0
    camera_params['offset_y'] = 0

    node = Node(
        package='spinnaker_camera_driver',
        executable='camera_driver_node',
        output='screen',
        name=[LaunchConfig('camera_name')],
        parameters=[
            camera_params,
            {
                'ffmpeg_image_transport.encoding': 'hevc_nvenc',
                'parameter_file': parameter_file,
                'serial_number': serial,
            },
        ],
        remappings=[
            ('~/control', '/exposure_control/control'),
        ],
    )

    return [node]


def generate_launch_description():
    """Create composable node by calling opaque function."""
    return LaunchDescription(
        [
            LaunchArg(
                'camera_name',
                default_value=['flir_camera'],
                description='camera name (ros node name)',
            ),
            LaunchArg(
                'camera_type',
                default_value='blackfly_s',
                description='type of camera (blackfly_s, chameleon...)',
            ),
            LaunchArg(
                'serial',
                default_value='auto',
                description='FLIR serial number or "auto" for auto-detection',
            ),
            LaunchArg(
                'parameter_file',
                default_value='',
                description='path to ros parameter definition file (override camera type)',
            ),
            LaunchArg(
                'image_width',
                default_value='1920',
                description='desired image width (binning calculated automatically)',
            ),
            LaunchArg(
                'image_height',
                default_value='1080',
                description='desired image height (binning calculated automatically)',
            ),
            OpaqueFunction(function=launch_setup),
        ]
    )
