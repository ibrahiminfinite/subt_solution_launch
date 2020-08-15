cmake_minimum_required(VERSION 2.8.3)
project(subt_solution_launch)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_filters
  pcl_conversions
  pcl_ros
  roscpp
  sensor_msgs
  tf2_ros
  #robot_localization
)

find_package(Boost REQUIRED)

set(IGN_MATH_VER 6)
find_package(ignition-math${IGN_MATH_VER} REQUIRED)
set(IGN_MSGS_VER 4)
find_package(ignition-msgs${IGN_MSGS_VER} REQUIRED)

catkin_package()

include_directories(
  ${Boost_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
)

add_executable(base_link_flattener
  src/base_link_costmap_projector.cpp
)

add_executable(point_cloud_filter
  src/pc_filter.cpp
)

target_link_libraries(base_link_flattener
  ${catkin_LIBRARIES}
)

target_link_libraries(point_cloud_filter
  ${catkin_LIBRARIES}
)

install(TARGETS
  base_link_flattener
  point_cloud_filter
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

install(DIRECTORY config/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
)

catkin_install_python(PROGRAMS  scripts/odom2base_transform_publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
