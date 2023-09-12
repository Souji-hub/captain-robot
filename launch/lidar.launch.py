import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='robot_pkg',
            executable='lidar_publisher',
            output='screen',
        )
    ])
