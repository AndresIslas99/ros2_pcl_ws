cmake_minimum_required(VERSION 3.8)
project(pointcloud_play)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(pcl_conversions REQUIRED)
find_package(PCL REQUIRED COMPONENTS common io filters)

add_executable(pass_through src/pass_through.cpp)

target_include_directories(pass_through PRIVATE ${PCL_INCLUDE_DIRS})
ament_target_dependencies(pass_through rclcpp sensor_msgs pcl_conversions)
target_link_libraries(pass_through ${PCL_LIBRARIES})

# 👇 esto instala el binario donde ros2 lo espera
install(TARGETS pass_through
  RUNTIME DESTINATION lib/${PROJECT_NAME}   # en Windows/Linux correcto
)
install(PROGRAMS
  scripts/pc_pub.py
  DESTINATION lib/${PROJECT_NAME}
)

# Instalar archivos de launch (para que 'ros2 launch' los encuentre)
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
