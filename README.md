# Bender
This is the main repository for Bender, the robot of the Boise State University Autonomous Robotic Systems team.
Bender is designed to compete at the NASA Lunabotics competition.
Bender is implemented using ROS2.

## Usage
### One-time Setup
Clone the repository onto a machine with ROS2 Iron installed.
If you have not already, initialize rosdep with the following command:
> sudo rosdep init

This only needs to be done once per computer.

### Building
Run the following script:
> ./make.sh

This script updates and installs all ROS dependencies needed, then compiles the project.
After running the script, you need to source the environment config in all terminal windows you are using:
> source install/setup.bash

Only run the script from the directory it is located in so that build artifacts don't end up where they shouldn't.
Rerun the script and source the environment config whenever you make any changes.

### Running
The project consists of multiple ROS2 packages, each found in their own directory under src/
Each package has a start script that launches that package individually.
There will eventually be scripts for launching the entire project at once.

