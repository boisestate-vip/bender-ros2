import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='bender_drive',
            executable='bender_drive',
            name='bender_drive'),
  ])
