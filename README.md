# ROS 2 + PCL — Point Clouds for Beginners

[![ROS 2](https://img.shields.io/badge/ROS%202-Humble-22314E?logo=ros&logoColor=white)](#)
[![Build](https://github.com/andresislas99/ros2_pcl_ws/actions/workflows/ci.yaml/badge.svg)](https://github.com/andresislas99/ros2_pcl_ws/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)

Workspace para **ROS 2 Humble** con un ejemplo mínimo de nubes de puntos:
- `pointcloud_play`: publica `/points_in`, filtra con **PCL PassThrough** y saca `/points_out`.
- **Launch** único para arrancar publisher + filtro + **RViz2**.
- Entorno por carpeta con **direnv** (opcional).

> Ideal para empezar, demos y CI: no requiere sensor físico.

---

## Tabla de contenidos
- [Demo rápida](#demo-rápida)
- [Requisitos e instalación](#requisitos-e-instalación)
- [Uso](#uso)
- [¿Por qué así?](#por-qué-así)
- [Documentación](#documentación)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

---

## Demo rápida

```bash
# 1) Clonar
git clone https://github.com/<YOUR_GITHUB_USER>/ros2_pcl_ws.git
cd ros2_pcl_ws

# 2) (opcional) Activar entorno por proyecto
direnv allow     # una sola vez

# 3) Dependencias del paquete (futuras)
rosdep install --from-paths src -r -y

# 4) Compilar
colcon build --symlink-install

# 5) Cargar overlay (si NO usas direnv)
source install/setup.bash

# 6) Lanzar demo
ros2 launch pointcloud_play demo.launch.py
```

**RViz2**
- `Fixed Frame`: `map`
- Visualización **PointCloud2** → Topic: `/points_out` (principal) y `/points_in` (opcional)

---

## Requisitos e instalación

- Ubuntu 22.04 + **ROS 2 Humble**
- `libpcl-dev`, `ros-humble-pcl-ros`, `ros-humble-pcl-conversions`
- (Opcional) `direnv` para activar el entorno al entrar a la carpeta

> Pasos detallados: [docs/INSTALL.md](docs/INSTALL.md)

---

## Uso

- **Launch recomendado**
  ```bash
  ros2 launch pointcloud_play demo.launch.py
  ```
- **Manual (3 terminales)**
  ```bash
  ros2 run pointcloud_play pc_pub.py       # publisher
  ros2 run pointcloud_play pass_through    # filtro
  rviz2                                    # visualizador
  ```
- **Introspección**
  ```bash
  ros2 topic list
  ros2 topic echo /points_out --once
  ros2 interface show sensor_msgs/msg/PointCloud2
  ```

> Más ejemplos y tips: [docs/USAGE.md](docs/USAGE.md)

---

## ¿Por qué así?

- Publisher sintético → reproducible sin hardware.
- Filtro PassThrough → primer bloque típico en pipelines 3D.
- Launch unificado → menor fricción para empezar.
- `direnv` → entorno por carpeta sin “ensuciar” otros proyectos.

Detalles y extensiones: [docs/OVERVIEW.md](docs/OVERVIEW.md)

---

## Documentación

- [Instalación](docs/INSTALL.md)
- [Entorno con direnv](docs/ENVIRONMENT.md)
- [Compilación (clean/flags)](docs/BUILD.md)
- [Uso y RViz2](docs/USAGE.md)
- [FAQ / Troubleshooting](docs/TROUBLESHOOTING.md)
- [CI con GitHub Actions](docs/CI.md)
- [Guía para publicar y mantener el repo](docs/GITHUB.md)

---

## Contribuir

Lee [CONTRIBUTING.md](CONTRIBUTING.md) y abre un issue/PR.
Plantillas disponibles en `.github/`.

---

## Licencia

MIT — ver [LICENSE.md](LICENSE.md).
