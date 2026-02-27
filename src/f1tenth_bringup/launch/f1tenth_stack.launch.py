import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    # 1. ZED2i Camera Node (Includes the official Stereolabs launch file)
    zed_wrapper_dir = get_package_share_directory('zed_wrapper')
    zed_launch_path = os.path.join(zed_wrapper_dir, 'launch', 'zed_camera.launch.py')
    
    zed_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(zed_launch_path),
        launch_arguments={
            'camera_model': 'zed2i',
            # You can pass other ZED parameters here as needed
        }.items()
    )

    # 2. Vision Perception Node (Your custom Python script)
    perception_node = Node(
        package='vision_perception',
        executable='line_mapper', # The name you will define in setup.py
        name='vision_perception_node',
        output='screen'
    )

    # 3. Control Planning Node (Your custom C++ script)
    control_node = Node(
        package='control_planning',
        executable='kart_controller', # The name you will define in CMakeLists.txt
        name='control_planning_node',
        output='screen'
    )

    # 4. VESC Driver Node (From the apt-get install)
    vesc_node = Node(
        package='vesc_driver',
        executable='vesc_driver_node',
        name='vesc_driver',
        output='screen',
        parameters=[
            {'port': '/dev/ttyACM0'}, # Update this to your physical VESC port
        ]
    )

    # Return the LaunchDescription object containing all nodes
    return LaunchDescription([
        zed_node,
        perception_node,
        control_node,
        vesc_node
    ])