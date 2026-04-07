cmake_minimum_required(VERSION 3.10)

# Set the project name and version
project(Dark_Spaces VERSION 0.1.0)

# Find Python package and development libraries
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# Specify the Python module name
set(PYTHON_MODULE_NAME Dark_Spaces)

# Add the source files (C code)
add_library(${PYTHON_MODULE_NAME} MODULE src/main.cxx)

# Set the include directories
target_include_directories(${PYTHON_MODULE_NAME} PRIVATE ${Python3_INCLUDE_DIRS})

# Link the necessary libraries
target_link_libraries(${PYTHON_MODULE_NAME} PRIVATE ${Python3_LIBRARIES})

# Set the module suffix (e.g., .so on Linux, .pyd on Windows)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_INSTALL_RPATH "$ORIGIN")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH ON)
set(CMAKE_BUILD_RPATH_USE_ORIGIN ON)
find_package(Threads REQUIRED)
find_package(absl REQUIRED)
find_package(protobuf REQUIRED)
find_package(gRPC REQUIRED)
set(ABSL_PROPAGATE_CXX_STD ON)
set_target_properties(${PYTHON_MODULE_NAME} PROPERTIES
PREFIX ""
SUFFIX ".${Python3_EXT_SUFFIX}"
)

# Install the Python module
#install(TARGETS ${PYTHON_MODULE_NAME} DESTINATION ${Python3_SITE_PACKAGES})
