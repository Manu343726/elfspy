cmake_minimum_required(VERSION 3.0)
project(elfspy)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQURIED ON)

set(ELFSPY_INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/include")
set(ELFSPY_PRIVATE_INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/include/elfspy")

add_subdirectory(src)
