#!/usr/bin/env python3
import time
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2  # helpers para construir PointCloud2


class CloudPublisher(Node):
    def __init__(self):
        super().__init__('pc_pub')
        self.pub = self.create_publisher(PointCloud2, '/points_in', 10)
        self.timer = self.create_timer(0.1, self.tick)  # 10 Hz
        self.t0 = time.time()
        self.get_logger().info('Publicando /points_in (XYZ)')

    def tick(self):
        t = time.time() - self.t0

        # malla de puntos
        xs = np.linspace(-2.0, 2.0, 160, dtype=np.float32)
        ys = np.linspace(-2.0, 2.0, 120, dtype=np.float32)
        x, y = np.meshgrid(xs, ys)
        z = 0.5 * np.sin(1.5 * x + t) + 0.5  # rango ~[0, 1]

        # puntos -> lista de tuplas (x, y, z)
        pts = np.stack((x, y, z), axis=-1).reshape(-1, 3).tolist()

        # Header correcto
        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = 'map'  # ajusta si quieres otro frame

        # construir mensaje
        msg = point_cloud2.create_cloud_xyz32(header, pts)
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = CloudPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
