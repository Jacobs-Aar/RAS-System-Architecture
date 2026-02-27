# Base image from Stereolabs with ZED SDK 4.1, CUDA 12.1, and Ubuntu 22.04
FROM stereolabs/zed:4.1-gl-devel-cuda12.1-ubuntu22.04

# Prevent interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Install ROS2 Humble
RUN apt-get update && apt-get install -y software-properties-common curl locales && \
    locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null && \
    apt-get update && apt-get install -y \
    ros-humble-desktop \
    ros-dev-tools \
    ros-humble-ackermann-msgs \
    ros-humble-vesc \
    ros-humble-vesc-msgs \
    ros-humble-vesc-driver \
    ros-humble-vesc-ackermann \
    python3-pip \
    python3-colcon-common-extensions \
    build-essential \
    cmake \
    git \
    libusb-1.0-0-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies for your CV and Control scripts
RUN pip3 install numpy opencv-python numba

# Setup ROS2 workspace directory
RUN mkdir -p /ros2_ws/src
WORKDIR /ros2_ws

# Source ROS2 automatically when opening a bash terminal in the container
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "if [ -f /ros2_ws/install/setup.bash ]; then source /ros2_ws/install/setup.bash; fi" >> ~/.bashrc

CMD ["/bin/bash"]