# Troubleshooting (FAQ)

## No se ve nada en RViz
- Fixed Frame = `map`
- Topic de PointCloud2 = `/points_out`
- Verifica datos:
  ```bash
  ros2 topic echo /points_out --once
  ```

## No aparecen ejecutables
```bash
source install/setup.bash
ros2 pkg executables pointcloud_play
```

## Errores de Python / catkin_pkg al compilar
Reconstruye fijando el intérprete:
```bash
rm -rf build/ install/ log/
colcon build --symlink-install   --cmake-args -DPython3_EXECUTABLE=$(which python3)
```

## Choque entre APT y pip
- No instales wrappers de ROS con `pip`.
- Usa APT para rclpy/pcl_ros; usa venv para dependencias de **aplicación**.
