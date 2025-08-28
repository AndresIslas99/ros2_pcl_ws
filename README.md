# ros2_pcl_ws — Point Cloud Playground (ROS 2 + PCL)

[![CI](https://img.shields.io/github/actions/workflow/status/AndresIslas99/ros2_pcl_ws/ci.yaml?branch=main)](https://github.com/AndresIslas99/ros2_pcl_ws/actions)
![ROS 2](https://img.shields.io/badge/ROS2-jazzy%7Chumble-blueviolet)
![License](https://img.shields.io/badge/license-Apache--2.0-informational)
[![Docs](https://img.shields.io/badge/docs-latest-brightgreen)](https://andresislas99.github.io/ros2_pcl_ws/)
[![Discussions](https://img.shields.io/badge/community-discussions-yellow)](https://github.com/AndresIslas99/ros2_pcl_ws/discussions)

## Demo
Filtrado **PassThrough** con PCL sobre `sensor_msgs/PointCloud2` y visualización en RViz2.  
_Inserta aquí una imagen o GIF: `docs/_static/demo.gif`_

## Características
- Publicador de ejemplo (Python) y filtro **PassThrough** (C++).
- Launch listo: `launch/demo.launch.py`.
- Estructura clara, CI, y docs publicadas con MkDocs Material.

## Instalación rápida
```bash
git clone https://github.com/AndresIslas99/ros2_pcl_ws.git
cd ros2_pcl_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

## Uso
```bash
# Demo: publicador de nubes + filtro passthrough
ros2 launch pointcloud_play demo.launch.py
```

### Parámetros clave
- `pass_through.field` (string, ej: `"z"`)
- `pass_through.limits` (float64[2], ej: `[0.0, 1.5]`)

## Estructura
```
docs/                 # instalación, build, uso, troubleshooting, CI, overview
src/pointcloud_play/  # package.xml, CMakeLists.txt, launch, nodos
.github/workflows/    # ci.yaml (ROS 2) y docs.yml (MkDocs)
```

## Roadmap
- Benchmarks: voxel grid, passthrough, RANSAC.
- Bags de ejemplo ligeros (LFS).
- Comparativas Jazzy vs Humble.

## Contribuir
Lee [CONTRIBUTING.md](CONTRIBUTING.md) y abre un [Discussion](https://github.com/AndresIslas99/ros2_pcl_ws/discussions) para ideas.

## Cita
Si te es útil, cita este repo como se indica en [CITATION.cff](CITATION.cff).
