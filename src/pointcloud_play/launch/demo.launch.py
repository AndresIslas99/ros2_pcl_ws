import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    cfg = os.path.join(
        get_package_share_directory("pointcloud_play"),
        "rviz",
        "points_demo.rviz"
    )

    return LaunchDescription([
        Node(
            package="pointcloud_play",
            executable="pc_pub.py",
            name="pc_pub",
            output="screen",
        ),
        Node(
            package="pointcloud_play",
            executable="pass_through",
            name="pass_through",
            output="screen",
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            arguments=["-d", cfg],
            output="screen",
        ),
    ])
