# Entorno por proyecto con direnv

Este repositorio incluye `.envrc` para:
- Crear un venv local que **reutiliza** librerías ROS de APT (no duplica rclpy/pcl_ros).
- Cargar `/opt/ros/humble/setup.bash` y `install/setup.bash` cuando existan.
- Limpiar al salir de la carpeta.

## Activar
```bash
direnv allow
```

## Sin direnv
Puedes trabajar a mano:
```bash
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```
