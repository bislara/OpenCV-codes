cmake_minimum_required(VERSION 2.8)
project(DisplayImage)
find_package( OpenCV REQUIRED )
add_executable( DisplayImage DisplayImage.cpp )
target_link_libraries( DisplayImage ${OpenCV_LIBS} )
add_executable( DisplayImage1 DisplayImage1.cpp )
target_link_libraries( DisplayImage1 ${OpenCV_LIBS} )

