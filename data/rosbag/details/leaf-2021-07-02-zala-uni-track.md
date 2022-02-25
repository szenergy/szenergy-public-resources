
```cs
path:        leaf-2021-07-02-zala-uni-track.bag
version:     2.0
duration:    17.4s
start:       Jul 02 2021 12:43:52.19 (1625222632.19)
end:         Jul 02 2021 12:44:09.56 (1625222649.56)
size:        1.2 GB
messages:    25524
compression: none [695/695 chunks]
types:       autoware_msgs/VehicleStatus     [77768c58b46a9120bd1fae64c52b3a77]
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
topics:      /cloud                                         434 msgs    : sensor_msgs/PointCloud2
             /current_pose                                  173 msgs    : geometry_msgs/PoseStamped
             /diagnostics                                    69 msgs    : diagnostic_msgs/DiagnosticArray (4 connections)
             /gps/duro/current_pose                         174 msgs    : geometry_msgs/PoseStamped
             /gps/duro/fix                                  173 msgs    : sensor_msgs/NavSatFix
             /gps/duro/imu                                 1716 msgs    : sensor_msgs/Imu
             /gps/duro/mag                                  429 msgs    : sensor_msgs/MagneticField
             /gps/nova/current_pose                         345 msgs    : geometry_msgs/PoseStamped
             /gps/nova/fix                                  341 msgs    : sensor_msgs/NavSatFix
             /gps/nova/imu                                 1721 msgs    : sensor_msgs/Imu
             /left_os1/os1_cloud_node/imu                  1735 msgs    : sensor_msgs/Imu
             /left_os1/os1_cloud_node/points                347 msgs    : sensor_msgs/PointCloud2
             /right_os1/os1_cloud_node/imu                 1734 msgs    : sensor_msgs/Imu
             /right_os1/os1_cloud_node/points               347 msgs    : sensor_msgs/PointCloud2
             /scan                                          433 msgs    : sensor_msgs/LaserScan
             /tf                                          10614 msgs    : tf2_msgs/TFMessage              (18 connections)
             /vehicle_speed_kmph                           1677 msgs    : std_msgs/Float32
             /vehicle_status                               1677 msgs    : autoware_msgs/VehicleStatus
             /velodyne_left/velodyne_points                 346 msgs    : sensor_msgs/PointCloud2
             /velodyne_right/velodyne_points                347 msgs    : sensor_msgs/PointCloud2
             /zed_node/left/camera_info                     346 msgs    : sensor_msgs/CameraInfo
             /zed_node/left/image_rect_color/compressed     346 msgs    : sensor_msgs/CompressedImage
```

![img](../img/leaf-2021-07-02-zala-uni-track_tf.svg)