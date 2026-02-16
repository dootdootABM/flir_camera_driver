from setuptools import find_packages
from setuptools import setup

setup(
    name='flir_camera_msgs',
    version='2.0.8',
    packages=find_packages(
        include=('flir_camera_msgs', 'flir_camera_msgs.*')),
)
