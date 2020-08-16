## SubT Challenge Mapping + explore_lite Exploration

### 1. Requirements
1.  rtabmap (tag : 0.20.0 melodic)
2.  rtabmap_ros (tag : 0.20.0 melodic)
3.  navigation (branch : master)

###2. Installation

To build the packages from source 
```
mkdir -p ~/subt_solution_ws/src
cd ~/subt_solution_ws/src

git clone -b 0.20.0-melodic https://github.com/ibrahiminfinite/rtabmap_ros.git
git clone -b 0.20.0-melodic https://github.com/ibrahiminfinite/rtabmap.git
git clone -b melodic-devel  https://github.com/ibrahiminfinite/navigation.git
git clone -b melodic-devel  https://github.com/ibrahiminfinite/m-explore.git
git clone -b explore_lite_navigation https://github.com/ibrahiminfinite/subt_solution_launch.git

cd ..
catkin_make_isolated -DCMAKE_INSTALL_PREFIX=~/subt_solution_ws/devel_isolated
```

##3. Running the solution

The solution consists of 2 parts at the moment
1. The SLAM system which consist of RTABmap that ouputs an occupancy grid
2. The navigation system move_base ros package

To bring up the solution, first source workspace overlays for each terminal

```
source /opt/ros/melodic/setup.bash
source ~/subt_solution_ws/devel_isolated/setup.bash
```

in Terminal 1,Run odometry transform publisher node 
```
rosrun subt_solution_launch odom2base_transform_publisher.py
```

in Terminal 2 , run rtabmap 
```
roslaunch subt_solution_launch rtabmap_2_Grid_demo.launch
```

in Terminal 3 , run navigation stack
```
roslaunch subt_solution_launch navigation.launch
```

in Terminal 4, run explore_lite
```
roslaunch subt_solution_launch husky_explore.launch
```


After above steps, open rviz
select MARBLE_HUSKY/map as the fixed frame
add the visualization as needed.
from pannels->tools properties, set the 2D NavGoal topic to MARBLE_HUSKY/move_base_simple/goal

finally use the 2D nav goal marker from the toolbar to select the goal in the map and watch the robot move.
