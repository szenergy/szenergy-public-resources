
```cs
path:         leaf-2021-04-23-campus.bag
version:      2.0
duration:     1:33s (93s)
start:        Apr 23 2021 13:42:57.28 (1619178177.28)
end:          Apr 23 2021 13:44:30.00 (1619178271.00)
size:         3.4 GB
messages:     153038
compression:  lz4 [3748/3748 chunks; 52.88%]
uncompressed: 6.4 GB @ 69.6 MB/s
compressed:   3.4 GB @ 36.8 MB/s (52.88%)
types:        autoware_msgs/VehicleStatus     [77768c58b46a9120bd1fae64c52b3a77]
              diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
              geometry_msgs/PoseStamped       [d3812c3cbc69362b77dc0b19b345f8f5]
              sensor_msgs/CameraInfo          [c9a58c1b0b154e0e6da7578cb991d214]
              sensor_msgs/CompressedImage     [8f7a12909da2c9d3332d540a0977563f]
              sensor_msgs/Imu                 [6a62c6daae103f4ff57a132d6f95cec2]
              sensor_msgs/LaserScan           [90c7ef2dc6895d81024acba2ac42f369]
              sensor_msgs/MagneticField       [2f3b0b43eed0c9501de0fa3ff89a45aa]
              sensor_msgs/NavSatFix           [2d3a8cd499b9b4a0249fb98fd05cfa48]
              sensor_msgs/PointCloud2         [1158d486dd51d683ce2f1be655c3c181]
              std_msgs/Float32                [73fcbf46b49191e672908e50842a83d4]
              tf2_msgs/TFMessage              [94810edda583a504dfda3829e70d7eec]
topics:       /cloud                                        4665 msgs    : sensor_msgs/PointCloud2
              /diagnostics                                   370 msgs    : diagnostic_msgs/DiagnosticArray (4 connections)
              /gps/duro/current_pose                         938 msgs    : geometry_msgs/PoseStamped
              /gps/duro/fix                                  938 msgs    : sensor_msgs/NavSatFix
              /gps/duro/imu                                 9290 msgs    : sensor_msgs/Imu
              /gps/duro/mag                                 2321 msgs    : sensor_msgs/MagneticField
              /gps/nova/current_pose                        1770 msgs    : geometry_msgs/PoseStamped
              /gps/nova/fix                                 1527 msgs    : sensor_msgs/NavSatFix
              /gps/nova/imu                                 8744 msgs    : sensor_msgs/Imu
              /imu_raw                                     23453 msgs    : sensor_msgs/Imu
              /left_os1/os1_cloud_node/imu                  9367 msgs    : sensor_msgs/Imu
              /left_os1/os1_cloud_node/points               1874 msgs    : sensor_msgs/PointCloud2
              /right_os1/os1_cloud_node/imu                 9367 msgs    : sensor_msgs/Imu
              /right_os1/os1_cloud_node/points              1873 msgs    : sensor_msgs/PointCloud2
              /scan                                         4665 msgs    : sensor_msgs/LaserScan
              /tf                                          47929 msgs    : tf2_msgs/TFMessage              (17 connections)
              /vehicle_speed_kmph                           8237 msgs    : std_msgs/Float32
              /vehicle_status                               8237 msgs    : autoware_msgs/VehicleStatus
              /velodyne_left/velodyne_points                1872 msgs    : sensor_msgs/PointCloud2
              /velodyne_right/velodyne_points               1873 msgs    : sensor_msgs/PointCloud2
              /zed_node/left/camera_info                    1864 msgs    : sensor_msgs/CameraInfo
              /zed_node/left/image_rect_color/compressed    1864 msgs    : sensor_msgs/CompressedImage
```

![img](../img/leaf-2021-04-23-campus_tf.svg)