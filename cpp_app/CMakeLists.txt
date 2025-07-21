cmake_minimum_required(VERSION 3.10)
project(count_pairs)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(count_pairs src/count_pairs.cpp)

install(TARGETS count_pairs DESTINATION bin)