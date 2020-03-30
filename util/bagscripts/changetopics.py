import rosbag
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Input bag file")
    parser.add_argument("--outdir", help="Output directory")
    parser.add_argument("--fileprefix", help="Output directory")
    args = parser.parse_args()
    inbagfilename = args.file
    outdir = args.outdir
    fileprefix = args.fileprefix
    ouster_left  = []
    ouster_right = []
    print("Loading BAG file: {0}".format(inbagfilename)) 
    in_bag = rosbag.Bag(inbagfilename)  
    
    outfilename = outdir+fileprefix+inbagfilename.split('/')[-1]
    print("Writing to: {0}".format(outfilename))
    with rosbag.Bag(outfilename, 'w') as c_bag:
        # Read messages in
        print("Swapping RIGHT and LEFT OUSTER LIDAR messages")        
        for topic, msg, t in in_bag.read_messages():
            if topic == "/right_os1/os1_cloud_node/points":
                ouster_left.append((msg, t))
            elif topic == "/left_os1/os1_cloud_node/points":
                ouster_right.append((msg, t))
            else:
                c_bag.write(topic, msg, t)
        # Push Ouster LEFT
        print("Writing swapped LEFT OUSTER LIDAR messages")
        for msg, t in ouster_left:
            msg.header.frame_id = "left_os1/os1_lidar"
            c_bag.write("/left_os1/os1_cloud_node/points", msg, t)
        # Push Ouster RIGHT
        print("Writing swapped RIGHT OUSTER LIDAR messages")
        for msg, t in ouster_right:
            msg.header.frame_id = "right_os1/os1_lidar"
            c_bag.write("/right_os1/os1_cloud_node/points", msg, t)
        print("Finished, writing, closing file...")
    print("\nDone!")


if __name__=="__main__":
    main()