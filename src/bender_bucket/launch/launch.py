import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='bender_bucket',
            executable='bender_bucket',
            name='bender_bucket'),
  ])
