import argparse
import glob
import os
import numpy as np
import open3d as o3d

# 시각화를 위한 플래그 설정, True로 설정하면 시각화 가능
visualize_on = False

# 시각화할 때 배경색을 검은색으로 변경하는 함수
def change_background_to_black(vis):
        opt = vis.get_render_option()
        opt.background_color = np.asarray([0, 0, 0])
        return False

# 주어진 ROI(Region of Interest) 내의 포인트만 필터링하는 함수 
def pass_through_filter(roi, pcd):
    points = np.asarray(pcd.points)
    x_range = np.logical_and(points[:,0] >= roi["x"][0] ,points[:,0] <= roi["x"][1])
    y_range = np.logical_and(points[:,1] >= roi["y"][0] ,points[:,1] <= roi["y"][1])
    z_range = np.logical_and(points[:,2] >= roi["z"][0] ,points[:,2] <= roi["z"][1])

    pass_through_filter = np.logical_and(x_range,np.logical_and(y_range,z_range))
    temp = o3d.geometry.PointCloud()
    temp.points = o3d.utility.Vector3dVector(points[pass_through_filter])
    return temp

# 반지름이 ROI 내에 있는 포인트만 필터링하는 함수 
def pass_through_filter_radious(roi, pcd):
    points = np.asarray(pcd.points)
    pass_through_filter = (np.sqrt(np.multiply(points[:,0],points[:,0]) + np.multiply(points[:,1],points[:,1])+np.multiply(points[:,2],points[:,2])) < roi["r"][0])
    temp = o3d.geometry.PointCloud()
    temp.points = o3d.utility.Vector3dVector(points[pass_through_filter])
    return temp


# ROI 추출 함수 
def extract_roi(roi, pcd):
    # pcd_filtered = pass_through_filter(roi,pcd) # pcd_filtered는 선택한 영역 내의 포인트 클라우드 데이터가 된다고함.
    pcd_filtered = pass_through_filter_radious(roi,pcd)
    return pcd_filtered

# 통계적 이상치 제거를 사용하여 노이즈 제거함수  
def noise_removal(pcd):
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
    pcd_filtered = pcd.select_by_index(ind)
    
    return pcd_filtered

# 필터링된 point cloud와 해당 인덱스와 파일 이름을 사용해 결과 저장함수  
def save_pointcloud(pcd,ind,file_name,  folder):
    if not os.path.exists(folder):
        os.makedirs(folder )
    if not os.path.exists(folder + '/lidar/'):
        os.makedirs(folder + '/lidar/')
    if not os.path.exists(folder + '/label/'):
        os.makedirs(folder + '/label/')

    lidar_name = folder + '/lidar/' + str(ind) +'_'+file_name+ '.txt'
    anno_name = folder + '/label/' + str(ind) +'_'+file_name+ '.json'
    
    xyz = np.asarray(pcd.points)
    xyz = np.hstack((xyz,np.ones((xyz.shape[0],1),dtype=xyz.dtype)))
    
    np.savetxt(lidar_name, xyz,delimiter=',')
    
    anno_file = open(anno_name, "w") 
    anno_file.write("{\n}")
    anno_file.close()
    
def run(args):
    path = args['pcd_path']
    
    pcd_list =  glob.glob(path+ '/pointcloud/'+'/*')
    nFiles   = len(pcd_list)
    
    roi = {"x":[-20.0,20.0],
        "y":[-20.0,20.0],
        "z":[-10.0,10.0]}
    
    roi_radious = {"r":[18]}
    
    dataset_dir = "./dataset/process_data"
    
    for i in range(0,nFiles):
        pcd = o3d.io.read_point_cloud(pcd_list[i])
            
        roi_pcd = extract_roi(roi_radious, pcd)

        noise_removal_pcd = noise_removal(roi_pcd)
        
        
        save_pointcloud(pcd, i,"1raw", dataset_dir)
        save_pointcloud(roi_pcd, i, "2roi",dataset_dir)
        save_pointcloud(noise_removal_pcd, i, "3noise_removal",dataset_dir)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p2', '--pcd-path', help="Path to the pcd file", required=True, default="./parsing_pcap")
    
    args = vars(parser.parse_args())
    run(args)
    