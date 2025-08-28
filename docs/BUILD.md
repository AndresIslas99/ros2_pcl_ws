# Compilación

## Normal
```bash
colcon build --symlink-install
```

## Limpia + fijar Python (si mezclaste intérpretes)
```bash
rm -rf build/ install/ log/
colcon build --symlink-install   --cmake-args -DPython3_EXECUTABLE=$(which python3)
```
