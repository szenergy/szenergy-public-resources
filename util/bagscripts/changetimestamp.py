import rosbag
import argparse

def main():    
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Input bag file')
    parser.add_argument('--outdir', help='sum the integers (default: find the max)')
    parser.add_argument('--fileprefix', help='sum the integers (default: find the max)')
    args = parser.parse_args()
    bag_name = args.file
    dir_name = args.outdir
    file_prefix = args.fileprefix
    first_run_o = True
    first_run_v = True
    print("Formating timestamps in: {0} into output directory: {1}, with prefix {2}".format(bag_name, dir_name, file_prefix))
    with rosbag.Bag(dir_name + file_prefix + bag_name, "w") as outbag:
        for topic, msg, t in rosbag.Bag(dir_name + bag_name).read_messages():
            if topic == "/velodyne_left/velodyne_points":
                if first_run_v:
                    velo_time = msg.header.stamp
                    first_run_v = False
            if topic == "/right_os1/os1_cloud_node/points":
                if first_run_o:
                    oust_time = msg.header.stamp
                    first_run_o = False
        print("Time diff: " + str(velo_time - oust_time))
        time_diff = velo_time - oust_time
        for topic, msg, t in rosbag.Bag(dir_name + bag_name).read_messages():
            if topic == "/right_os1/os1_cloud_node/points" or topic == "/left_os1/os1_cloud_node/points":
                    msg2 = msg
                    msg2.header.stamp = msg.header.stamp + time_diff
                    outbag.write(topic, msg2, t)
            else:
                outbag.write(topic, msg, t)
    print(dir_name + file_prefix + bag_name + " .... ok")


if __name__=="__main__":
    main()