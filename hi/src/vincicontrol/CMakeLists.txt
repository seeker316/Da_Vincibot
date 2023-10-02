cmake_minimum_required(VERSION 3.0.2)
project(vincicontrol)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

################################################
## Declare ROS messages, services, and actions ##
################################################

## To declare and build messages, services, or actions from within this
## package, follow these steps:

## 1. Create your message files in the 'msg' folder (uncomment and modify as needed)
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## 2. Create your service files in the 'srv' folder (uncomment and modify as needed)
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## 3. Create your action files in the 'action' folder (uncomment and modify as needed)
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## 4. Generate added messages and services with any dependencies listed here
# generate_messages(
#   DEPENDENCIES
#   std_msgs  # Or other packages containing msgs
# )

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

## To declare and build dynamic reconfigure parameters within this
## package, follow these steps:

## 1. Create your dynamic reconfigure parameter files in the 'cfg' folder (uncomment and modify as needed)
# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
#   cfg/DynReconf2.cfg
# )

###################################
## catkin specific configuration ##
###################################

catkin_package(
  CATKIN_DEPENDS rospy roscpp
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Uncomment and modify as needed to declare libraries and executables

# add_library(${PROJECT_NAME}
#   src/${PROJECT_NAME}/vincibotcontrol.cpp
# )

# add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

# add_executable(${PROJECT_NAME}_node src/vincibotcontrol_node.cpp)

# set_target_properties(${PROJECT_NAME}_node PROPERTIES OUTPUT_NAME node PREFIX "")

# add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

# target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# Uncomment and modify as needed to specify installation targets

# install(TARGETS ${PROJECT_NAME}_node
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

# install(TARGETS ${PROJECT_NAME}
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
# )

# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

# Uncomment and modify as needed to add tests

# catkin_add_gtest(${PROJECT_NAME}-test test/test_vincibotcontrol.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

# catkin_add_nosetests(test)

