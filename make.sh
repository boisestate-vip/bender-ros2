#! /bin/bash

RED='\033[0;31m'
NC='\033[0m'

rosdep update
rosdep install --from-paths src -y --ignore-src

colcon build

printf "\n\n${RED}DON'T FORGET TO RUN THE FOLLOWING:${NC} source install/setup.bash\n\n"
