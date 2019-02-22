# Szenergy public resources
This repository is devoted to share data related to the Shell Eco-marathon __Autonomous__ Urban Concept (AUC) challange. 

#### Table of contents:
- [Datasets](#datasets)
- [Simulations](#simulations)
- [Algorithms](#algorithms)
- [Papers](#papers)

## Datasets

![img](img/dataset-example-small.png)

- The data is available: [www.sze.hu/~herno/PublicDataAutonomous](http://www.sze.hu/~herno/PublicDataAutonomous/)

- The data is in `.bag` format, the standard logging format for ROS and it can be also imported to MATLAB. 

- The different rosbag files contain different topics, but the most important topics of the rosbag files are:

  - `/gps/odom`: position in xyz and orientation xyzw (message type: `nav_msgs/Odometry`)
  - `/gps/status`: the sum of all visible satelites (message type: `sensor_msgs/NavSatStatus`)
  - `/gps/kvhstatus`: sum of all kvh gps error, so 0 is means no errors (message type: `std_msgs/Int8`)
  - `/gps/fix`: timestamp, latitude, longitude, altitude (message type: `sensor_msgs/NavSatFix`)
  - `/gps/utmzone`: the utm zone, it should be `33T` in Hungary (message type: `std_msgs/String`)
  - `/gps/current_pose`: the current pose (message type: `geometry_msgs/PoseStamped`)
  - `/velodyne_points`: the point cloud of the Velodyne Puck VLP16 LIDAR (message type: `sensor_msgs/PointCloud2`)
  - `/leaf/current_velocity`: the current velocity from CAN (message type: ` geometry_msgs/TwistStamped`)
  - `/leaf/is_autonomous`: weather it is autonomous (message type: `std_msgs/Bool`)
  - `/leaf/throttle_pos`: percentage of the throttle (message type: `std_msgs/Float64`)
  - `/lane_waypoints_array`: lane waypoints from autoware (message type: `autoware_msgs/LaneArray`)
  - `/global_waypoints_mark`: autoware global waypoints (message type: `visualization_msgs/MarkerArray`)
  - `/local_waypoints_mark`: autoware local waypoints (message type: `visualization_msgs/MarkerArray`)
  - `/camera_image`: the camera image (message type: `sensor_msgs/CompressedImage`)

## Simulations

- In this section Gazebo and V-REP simulations will be available.

## Algorithms

- Algorithms will be available later.

## Papers

- Papers will be available later.
