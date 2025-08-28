# Uso

## Demo (launch)
```bash
ros2 launch pointcloud_play demo.launch.py
```

### RViz2
- Fixed Frame: `map`
- PointCloud2 → `/points_out` (y opcional `/points_in`)

## Manual
```bash
ros2 run pointcloud_play pc_pub.py
ros2 run pointcloud_play pass_through
rviz2
```

## Introspección
```bash
ros2 topic list
ros2 topic echo /points_out --once
ros2 interface show sensor_msgs/msg/PointCloud2
```
