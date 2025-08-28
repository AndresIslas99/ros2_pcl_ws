# CI

Workflow en `.github/workflows/ci.yaml`:
- Ubuntu 22.04
- Setup ROS 2 Humble
- `colcon build` del paquete

Amplía con tests (gtest/pytest), ament_lint y artefactos de logs.
