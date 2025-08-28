#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/point_cloud2.hpp>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/filters/passthrough.h>

class PassThroughNode : public rclcpp::Node {
public:
  PassThroughNode() : Node("pass_through_node") {
    sub_ = this->create_subscription<sensor_msgs::msg::PointCloud2>(
      "/points_in", 10,
      std::bind(&PassThroughNode::cb, this, std::placeholders::_1));
    pub_ = this->create_publisher<sensor_msgs::msg::PointCloud2>("/points_out", 10);
    RCLCPP_INFO(get_logger(), "PassThrough listo. Sub: /points_in Pub: /points_out");
  }

private:
  void cb(const sensor_msgs::msg::PointCloud2::SharedPtr msg) {
    // ROS2 msg -> PCL
    pcl::PointCloud<pcl::PointXYZ>::Ptr pcl_in(new pcl::PointCloud<pcl::PointXYZ>);
    pcl::fromROSMsg(*msg, *pcl_in);

    // Filtro simple: Z en [0.0, 3.0] m
    pcl::PassThrough<pcl::PointXYZ> pass;
    pass.setInputCloud(pcl_in);
    pass.setFilterFieldName("z");
    pass.setFilterLimits(0.0, 3.0);
    pcl::PointCloud<pcl::PointXYZ>::Ptr pcl_out(new pcl::PointCloud<pcl::PointXYZ>);
    pass.filter(*pcl_out);

    // PCL -> ROS2 msg
    sensor_msgs::msg::PointCloud2 out;
    pcl::toROSMsg(*pcl_out, out);
    out.header = msg->header;
    pub_->publish(out);
  }

  rclcpp::Subscription<sensor_msgs::msg::PointCloud2>::SharedPtr sub_;
  rclcpp::Publisher<sensor_msgs::msg::PointCloud2>::SharedPtr pub_;
};

int main(int argc, char** argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<PassThroughNode>());
  rclcpp::shutdown();
  return 0;
}
