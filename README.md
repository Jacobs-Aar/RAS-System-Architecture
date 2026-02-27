# Autonomous Racing Stack: F1Tenth & Go-Kart

This is the central repository for our autonomous software stack. This repository contains the ROS2 architecture, Docker configurations, and operational documentation required to run the autonomous system. 

Currently, this stack is configured for deployment and testing on the **F1Tenth** platform, with an architectural roadmap to migrate to the full-scale autonomous go-kart.

---

## 📂 Repository Navigation

This repository is organized to separate documentation, container configurations, and ROS2 packages clearly:

* **`docs/`**: Detailed system documentation.
  * `architecture/system_overview.md`: High-level system data flow and core design decisions.
  * `docker/setup_guide.md`: Explanations of container dependencies, base images (e.g., ZED SDK), and compose configurations.
  * `hardware/hardware_specs.md`: Sensor breakdowns (e.g., ZED2i 120° FOV) and compute limitations.
  * `ros2_stack/node_architecture.md`: ROS2 node graph, publish/subscribe topics, and custom message types.
  * `ros2_stack/`: Details on the 4-node core pipeline:
    **`zed_wrapper`** (Third-Party): Publishes raw video, depth, and point clouds from the ZED2i.
    **`vision_perception`** (Custom): Subscribes to the video/depth, performs line detection, and publishes a 2D top-down map.
    **`control_planning`** (Custom): Subscribes to the 2D map, calculates pathing, and publishes `AckermannDriveStamped` commands.
    **`vesc_driver`** (Third-Party): Translates Ackermann commands into physical actuator movements.
* **`docker/`**: Environment configurations.
  * `f1tenth/`: Dockerfiles and compose setups for the 1:10 scale testbed.
  * `go_kart/`: (WIP) Future container configurations for the full-scale vehicle.
* **`scripts/`**: Utility scripts for environment setup and networking.
  * `f1tenth/`: Host-machine setup scripts for the scale car.
  * `go_kart/`: (WIP) Setup scripts for the full-scale compute unit.
* **`src/`**: The unified ROS2 workspace. Core perception and control packages are shared, while `_bringup` packages handle vehicle-specific launch configurations.

---

## 🐧 Linux Environment Setup

The primary deployment target for this stack is a Linux environment (e.g., Ubuntu 22.04). The entire ROS2 workspace is containerized to prevent dependency conflicts on the host machine.

### 1. Prerequisites
Ensure your Linux host has the following installed:
* [Git](https://git-scm.com/downloads)
* [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
* [Docker Compose](https://docs.docker.com/compose/install/linux/)
* [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

### 2. Pulling the Repository
Clone the repository and its submodules to your local machine:
```bash
git clone https://github.com/Jacobs-Aar/RAS-System-Architecture
cd RAS-System-Architecture
```

### 3. Determining F1Tenth or Full-Scale Go-Kart

#### F1Tenth Deployment
The F1Tenth container environment includes the base ROS2 installation, standard drivers (VESC, LiDAR), and the custom autonomous workspace

##### Building and Running the Container
1. Navigate to the Docker directory:
```bash
cd docker/f1tenth
```

2. Build the Docker image:
```bash
docker compose build
```

3. Launch the stack
```bash
docker compose up -d
```

4. Access the running container:
```bash
docker exec -it f1tenth_core /bin/bash
```

5. Build the ROS2 Workspace (Insider the Container):
```bash
cd /ros2_ws
colcon build --symlink-install
source install/setup.bash
```

#### Go-Kart Deployment
##### This section is reserved for when the Go-Kart is being implemented and migrated to from the F1Tenth architecture