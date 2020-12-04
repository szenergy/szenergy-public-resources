
```cs
path:         leaf-2020-06-10-campus.bag
version:      2.0
duration:     35.7s
start:        Jun 10 2020 17:00:49.00 (1591801249.00)
end:          Jun 10 2020 17:01:24.74 (1591801284.74)
size:         2.4 GB
messages:     66585
compression:  lz4 [1961/1961 chunks; 55.26%]
uncompressed: 4.3 GB @ 122.1 MB/s
compressed:   2.4 GB @  67.5 MB/s (55.26%)
types:        autoware_msgs/VehicleStatus [77768c58b46a9120bd1fae64c52b3a77]
              geometry_msgs/PoseStamped   [d3812c3cbc69362b77dc0b19b345f8f5]
              nav_msgs/Odometry           [cd5e73d190d741a2f92e81eda573aca7]
              sensor_msgs/CameraInfo      [c9a58c1b0b154e0e6da7578cb991d214]
              sensor_msgs/Image           [060021388200f6f0f447d0fcd9c64743]
              sensor_msgs/Imu             [6a62c6daae103f4ff57a132d6f95cec2]
              sensor_msgs/LaserScan       [90c7ef2dc6895d81024acba2ac42f369]
              sensor_msgs/PointCloud2     [1158d486dd51d683ce2f1be655c3c181]
              tf2_msgs/TFMessage          [94810edda583a504dfda3829e70d7eec]
topics:       /cloud                              1777 msgs    : sensor_msgs/PointCloud2    
              /current_pose                        358 msgs    : geometry_msgs/PoseStamped  
              /gps/duro/current_pose               358 msgs    : geometry_msgs/PoseStamped  
              /left_os1/os1_cloud_node/imu        3574 msgs    : sensor_msgs/Imu            
              /left_os1/os1_cloud_node/points      715 msgs    : sensor_msgs/PointCloud2    
              /right_os1/os1_cloud_node/imu       3573 msgs    : sensor_msgs/Imu            
              /right_os1/os1_cloud_node/points     715 msgs    : sensor_msgs/PointCloud2    
              /scan                               1779 msgs    : sensor_msgs/LaserScan      
              /tf                                42048 msgs    : tf2_msgs/TFMessage          (13 connections)
              /vehicle_status                     7743 msgs    : autoware_msgs/VehicleStatus
              /velodyne_left/velodyne_points       714 msgs    : sensor_msgs/PointCloud2    
              /velodyne_right/velodyne_points      714 msgs    : sensor_msgs/PointCloud2    
              /zed_node/left/camera_info          1059 msgs    : sensor_msgs/CameraInfo     
              /zed_node/odom                       928 msgs    : nav_msgs/Odometry          
              /zed_node/rgb/image_rect_color       530 msgs    : sensor_msgs/Image
```

![img](../img/leaf-2020-06-10-campus_tf.svg)