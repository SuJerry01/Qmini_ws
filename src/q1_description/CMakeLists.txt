cmake_minimum_required(VERSION 3.8)
project(q1_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  urdf/
  DESTINATION share/${PROJECT_NAME}/urdf
)

install(DIRECTORY
  meshes/
  DESTINATION share/${PROJECT_NAME}/meshes
)

install(DIRECTORY
  launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

install(DIRECTORY
  config/
  DESTINATION share/${PROJECT_NAME}/config
)

ament_package()
