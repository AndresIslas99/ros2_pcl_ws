# Instalación

Objetivo: **Ubuntu 22.04** + **ROS 2 Humble**.

## 1) Herramientas base
```bash
sudo apt update
sudo apt install -y build-essential cmake git   python3-colcon-common-extensions python3-rosdep
sudo rosdep init 2>/dev/null || true
rosdep update
```

## 2) ROS 2 Humble
Sigue la guía oficial de ROS 2 Humble. Al final tendrás `/opt/ros/humble`.

## 3) PCL + bindings
```bash
sudo apt install -y libpcl-dev ros-humble-pcl-ros ros-humble-pcl-conversions
```

## 4) (Opcional) direnv
```bash
sudo apt install -y direnv
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
source ~/.bashrc
```

## 5) Clonar y compilar
```bash
git clone https://github.com/<YOUR_GITHUB_USER>/ros2_pcl_ws.git
cd ros2_pcl_ws
direnv allow        # opcional
rosdep install --from-paths src -r -y
colcon build --symlink-install
```
