import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf_file_name = LaunchConfiguration('urdf', default='q1.urdf')
    '''
    urdf_path = os.path.join(
        get_package_share_directory('q1_description'),
        'urdf')
    '''
    urdf_path = get_package_share_directory('q1_description')


    # Read URDF at launch time via a Command substitution equivalent
    # Here we resolve the default and read the file immediately for simplicity
    if os.path.exists(urdf_to_read):
        with open(urdf_to_read, 'r') as infp:
            robot_desc = infp.read()
    else:
        robot_desc = '<robot name="q1"></robot>'

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        DeclareLaunchArgument(
            'urdf',
            default_value='q1.urdf',
            description='URDF file name located in q1_description/urdf'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}]
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_package_share_directory('q1_description'), 'config', 'q1_config.rviz')]
        )
    ])


