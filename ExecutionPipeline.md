# 1. Navigate to your Docker environment
cd RAS-System-Architecture/docker/f1tenth

# 2. Build the image (pulls ROS2 Humble, ZED SDK, installs VESC drivers)
docker compose build

# 3. Start the container in the background
docker compose up -d

# 4. Attach to the running container to access the ROS2 environment
docker exec -it f1tenth_stack /bin/bash

# --- YOU ARE NOW INSIDE THE DOCKER CONTAINER ---

# 5. Navigate to the ROS2 workspace
cd /ros2_ws

# 6. Build the entire workspace (compiles your Python, C++, and launch files)
colcon build --symlink-install

# 7. Source the newly built workspace so ROS2 can find your nodes
source install/setup.bash

# 8. Launch the entire F1Tenth stack with the file we wrote earlier!
ros2 launch f1tenth_bringup f1tenth_stack.launch.py