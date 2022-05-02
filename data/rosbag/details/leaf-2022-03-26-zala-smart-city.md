```cs
path:         leaf-2022-03-26-zala-smart-city.bag
version:      2.0
duration:     1:01s (61s)
start:        Mar 26 2022 11:36:06.25 (1648290966.25)
end:          Mar 26 2022 11:37:07.92 (1648291027.92)
size:         1.2 GB
messages:     135640
compression:  lz4 [1370/1370 chunks; 45.28%]
uncompressed: 2.6 GB @ 42.8 MB/s
compressed:   1.2 GB @ 19.4 MB/s (45.28%)
types:        autoware_lanelet2_msgs/MapBin            [9d7c66d4c8e6e3f95a20131a6e37fe22]
              autoware_msgs/Centroids                  [2199cac4695ce1fc0f346db535dda30d]
              autoware_msgs/CloudClusterArray          [5bdd7c958335da845b88351aab5141d4]
              autoware_msgs/ControlCommandStamped      [cf8b01a8273bedcf082c4a0007472482]
              autoware_msgs/DetectedObjectArray        [c16aecef51c24c6808480a0295e47806]
              autoware_msgs/Lane                       [40bde126fe5f348ef74699a32398ac74]
              autoware_msgs/VehicleStatus              [77768c58b46a9120bd1fae64c52b3a77]
              dynamic_reconfigure/Config               [958f16a05573709014982821e6822580]
              dynamic_reconfigure/ConfigDescription    [757ce9d44ba8ddd801bb30bc456f946f]
              geometry_msgs/PoseStamped                [d3812c3cbc69362b77dc0b19b345f8f5]
              geometry_msgs/TwistStamped               [98d34b0043a2093cf9d9345ab6eef12e]
              geometry_msgs/Vector3                    [4a842b65f413084dc2b10fb484ea7f17]
              gps_common/GPSFix                        [3db3d0a7bc53054c67c528af84710b70]
              jsk_rviz_plugins/OverlayText             [7efc1ed34881f913afcee6ba02aa1242]
              nav_msgs/Odometry                        [cd5e73d190d741a2f92e81eda573aca7]
              novatel_gps_msgs/Inspva                  [f6fbcfee08847158b28edeb7f76b942f]
              novatel_gps_msgs/Inspvax                 [cebf3b182479d01907e3894361b97eba]
              novatel_gps_msgs/Insstdev                [5a3ffc9969b49cd107b55c9843133d1c]
              novatel_gps_msgs/NovatelCorrectedImuData [81ec3aad90f65315c03ad2199cdd99cf]
              novatel_gps_msgs/NovatelHeading2         [1195c3bddd7a9ddbaf770e688a2f354a]
              novatel_gps_msgs/NovatelUtmPosition      [401ec19560e710c1e0aab9f0eec02ece]
              novatel_gps_msgs/NovatelVelocity         [a8fb7d9232aaf68f98caa2b4cda2597b]
              sensor_msgs/CompressedImage              [8f7a12909da2c9d3332d540a0977563f]
              sensor_msgs/Imu                          [6a62c6daae103f4ff57a132d6f95cec2]
              sensor_msgs/MagneticField                [2f3b0b43eed0c9501de0fa3ff89a45aa]
              sensor_msgs/NavSatFix                    [2d3a8cd499b9b4a0249fb98fd05cfa48]
              sensor_msgs/PointCloud2                  [1158d486dd51d683ce2f1be655c3c181]
              sensor_msgs/TimeReference                [fded64a0265108ba86c3d38fb11c0c16]
              std_msgs/Float32                         [73fcbf46b49191e672908e50842a83d4]
              std_msgs/Float64MultiArray               [4b7d974086d4060e7db4613a7e6c3ba4]
              std_msgs/Int32                           [da5909fbe378aeaf85e547e830cc1bb7]
              std_msgs/String                          [992ce8a1687cec8c8bd883ec73ca41d1]
              std_msgs/UInt8                           [7c8164229e7d2c17eb95e9231617fdee]
              tf2_msgs/TFMessage                       [94810edda583a504dfda3829e70d7eec]
              visualization_msgs/Marker                [4048c9de2a16f4ae8e0538085ebf1b97]
              visualization_msgs/MarkerArray           [d155b9ce5188fbaf89745847fd5882d7]
topics:       /base_waypoints                                       620 msgs    : autoware_msgs/Lane                      
              /closest_waypoint                                     620 msgs    : std_msgs/Int32                          
              /closest_waypoints/visualization                      310 msgs    : visualization_msgs/Marker               
              /cluster_centroids                                   1240 msgs    : autoware_msgs/Centroids                 
              /converted_euclidean_objects                         1240 msgs    : visualization_msgs/MarkerArray          
              /ctrl_cmd                                            2068 msgs    : autoware_msgs/ControlCommandStamped     
              /ctrl_raw                                            2068 msgs    : autoware_msgs/ControlCommandStamped     
              /current_pose                                        1240 msgs    : geometry_msgs/PoseStamped               
              /current_pose_alt                                     621 msgs    : geometry_msgs/PoseStamped               
              /current_velocity                                    5087 msgs    : geometry_msgs/TwistStamped              
              /detected_object_centroid                             443 msgs    : visualization_msgs/MarkerArray          
              /detection/lidar_detector/cloud_clusters             1240 msgs    : autoware_msgs/CloudClusterArray         
              /detection/lidar_detector/objects                    1240 msgs    : autoware_msgs/DetectedObjectArray       
              /detection/lidar_detector/objects_markers            1240 msgs    : visualization_msgs/MarkerArray          
              /final_waypoints                                     1238 msgs    : autoware_msgs/Lane                      
              /global_waypoints/visualization                       619 msgs    : visualization_msgs/MarkerArray          
              /gnss_pose                                           1091 msgs    : geometry_msgs/PoseStamped               
              /gps/duro/current_pose                                618 msgs    : geometry_msgs/PoseStamped               
              /gps/duro/fix                                         618 msgs    : sensor_msgs/NavSatFix                   
              /gps/duro/imu                                        6124 msgs    : sensor_msgs/Imu                         
              /gps/duro/mag                                        1531 msgs    : sensor_msgs/MagneticField               
              /gps/duro/odom                                        618 msgs    : nav_msgs/Odometry                       
              /gps/duro/rollpitchyaw                                618 msgs    : geometry_msgs/Vector3                   
              /gps/duro/status_flag                                 618 msgs    : std_msgs/UInt8                          
              /gps/duro/status_string                               618 msgs    : std_msgs/String                         
              /gps/duro/time_ref                                    618 msgs    : sensor_msgs/TimeReference               
              /gps/nova/bestutm                                    1087 msgs    : novatel_gps_msgs/NovatelUtmPosition     
              /gps/nova/bestvel                                    1089 msgs    : novatel_gps_msgs/NovatelVelocity        
              /gps/nova/corrimudata                                5243 msgs    : novatel_gps_msgs/NovatelCorrectedImuData
              /gps/nova/current_pose                               1087 msgs    : geometry_msgs/PoseStamped               
              /gps/nova/fix                                         788 msgs    : sensor_msgs/NavSatFix                   
              /gps/nova/gps                                         788 msgs    : gps_common/GPSFix                       
              /gps/nova/heading2                                     54 msgs    : novatel_gps_msgs/NovatelHeading2        
              /gps/nova/imu                                        5161 msgs    : sensor_msgs/Imu                         
              /gps/nova/inspva                                     6008 msgs    : novatel_gps_msgs/Inspva                 
              /gps/nova/inspvax                                    6010 msgs    : novatel_gps_msgs/Inspvax                
              /gps/nova/insstdev                                     58 msgs    : novatel_gps_msgs/Insstdev               
              /lanelet2_map_viz                                       1 msg     : visualization_msgs/MarkerArray          
              /lanelet_map_bin                                        1 msg     : autoware_lanelet2_msgs/MapBin           
              /left_os1/os1_cloud_node/points                      1232 msgs    : sensor_msgs/PointCloud2                 
              /mpc_follower/debug/debug_values                     2053 msgs    : std_msgs/Float64MultiArray              
              /mpc_follower/debug/filtered_traj                    1215 msgs    : visualization_msgs/Marker               
              /mpc_follower/debug/mpc_calc_time                    2053 msgs    : std_msgs/Float32                        
              /mpc_follower/debug/predicted_traj                   2052 msgs    : visualization_msgs/Marker               
              /mpc_waypoints                                       1232 msgs    : autoware_msgs/Lane                      
              /obstacle_avoidance_params/parameter_descriptions       1 msg     : dynamic_reconfigure/ConfigDescription   
              /obstacle_avoidance_params/parameter_updates            1 msg     : dynamic_reconfigure/Config              
              /org                                                  443 msgs    : visualization_msgs/MarkerArray          
              /points_cluster                                      1231 msgs    : sensor_msgs/PointCloud2                 
              /points_ground                                       1231 msgs    : sensor_msgs/PointCloud2                 
              /points_lanes                                        1231 msgs    : sensor_msgs/PointCloud2                 
              /points_no_ground                                    1231 msgs    : sensor_msgs/PointCloud2                 
              /text_overlay                                        1228 msgs    : jsk_rviz_plugins/OverlayText            
              /tf                                                 37850 msgs    : tf2_msgs/TFMessage                       (19 connections)
              /tf_static                                              2 msgs    : tf2_msgs/TFMessage                       (2 connections)
              /transmissionstate                                   1140 msgs    : std_msgs/String                         
              /twist_raw                                           2048 msgs    : geometry_msgs/TwistStamped              
              /vehicle_speed_kmph                                  5125 msgs    : std_msgs/Float32                        
              /vehicle_status                                      5125 msgs    : autoware_msgs/VehicleStatus             
              /wheel_angle_deg                                     5125 msgs    : std_msgs/Float32                        
              /zed_node/left/image_rect_color/compressed           1210 msgs    : sensor_msgs/CompressedImage


```
