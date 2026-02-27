# Autonomous Racing Stack: F1Tenth & Go-Kart

This is the central repository for our autonomous software stack. This repository contains the ROS2 architecture, Docker configurations, and operational documentation required to run the autonomous system. 

Currently, this stack is configured for deployment and testing on the **F1Tenth** platform, with an architectural roadmap to migrate to the full-scale autonomous go-kart.

---

## 📂 Repository Navigation

This repository is organized to separate documentation, container configurations, and ROS2 packages clearly:

* **`docs/`**: Detailed documentation for the system.
    * `architecture/`: High-level system diagrams and data flow.
    * `hardware/`: Sensor integrations, wiring guides, and compute unit specs.
    * `ros2_stack/`: Details on perception, planning, and control nodes.
* **`docker/`**: Contains the Dockerfiles and `docker-compose.yml` files for isolated environments.
    * `f1tenth/`: Container setups specifically for the 1:10 scale car.
    * `go_kart/`: Container setups for the full-scale vehicle (WIP).
* **`scripts/`**: Utility scripts for environment setup, building workspaces, and launching nodes.
* **`src/`**: The main ROS2 workspace containing all custom packages and submodules.

---

## 🐧 Linux Environment Setup

The primary deployment target for this stack is a Linux environment (e.g., Ubuntu 22.04). The entire ROS2 workspace is containerized to prevent dependency conflicts on the host machine.

### 1. Prerequisites
Ensure your Linux host has the following installed:
* [Git](https://git-scm.com/downloads)
* [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
* [Docker Compose](https://docs.docker.com/compose/install/linux/)
* *(Optional)* NVIDIA Container Toolkit (if using GPU acceleration for ML/CV tasks)

### 2. Pulling the Repository
Clone the repository and its submodules to your local machine:
```bash
git clone https://github.com/Jacobs-Aar/RAS-System-Architecture
cd RAS-System-Architecture