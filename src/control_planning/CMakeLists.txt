cmake_minimum_required(VERSION 3.8)
project(control_planning)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(ackermann_msgs REQUIRED)

# -------------------------------------------------------------------
# TODO: Once your MATLAB port is done, place your C++ source code 
# in the src/ folder (e.g., src/kart_controller.cpp) and update below.
# -------------------------------------------------------------------

add_executable(kart_controller src/kart_controller.cpp)
target_include_directories(kart_controller PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)

# Link the ROS2 libraries to your executable
ament_target_dependencies(kart_controller
  rclcpp
  nav_msgs
  ackermann_msgs
)

# Install the executable so ROS2 can find it using 'ros2 run' or launch files
install(TARGETS
  kart_controller
  DESTINATION lib/${PROJECT_NAME})

# Install the include directory
install(DIRECTORY include/
  DESTINATION include)

ament_package()