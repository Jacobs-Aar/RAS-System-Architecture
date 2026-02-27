# Autonomous Racing Go-Kart Stack Documentation

Welcome to the documentation repository for the autonomous software stack. This repository houses all architectural references, setup guides, and operational instructions for running our ROS2 system within Docker environments, ensuring a seamless transition from local development to the physical compute unit on the kart.

## 📑 Table of Contents
- [Architecture Overview](docs/architecture/system_overview.md)
- [ROS2 Stack](docs/ros2_stack/)
  - [Perception](docs/ros2_stack/perception.md)
  - [Planning](docs/ros2_stack/planning.md)
  - [Control](docs/ros2_stack/control.md)
- [Docker Environment](docs/docker/setup_guide.md)
- [Hardware Interfaces](docs/hardware/interfaces.md)

## 🚀 Quick Start

To get the autonomous stack running locally, team members will need to utilize our Docker environment, which comes pre-configured with ROS2 and all necessary dependencies.

### Prerequisites
* [Docker Desktop](https://docs.docker.com/desktop/) (Ensure WSL2 backend is enabled if developing on Windows)
* (Optional) NVIDIA Container Toolkit for GPU acceleration

### Running the Stack

1. **Pull the latest images:**
   ```bash
   docker compose pull