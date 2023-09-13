from numpy import uint16
import argparse

# 아래의 세 변수는 RGB 컬러 맵핑을 위한 리스트.
soslab_r = [ 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 11, 12, 12, 13, 13, 14, 15, 15, 16, 16, 17, 18, 18, 19, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25, 25, 26, 27, 27, 28, 28, 29, 29, 30, 31, 31, 32, 32, 33, 34, 34, 35, 35, 36, 37, 37, 38, 38, 39, 40, 40, 41, 41, 42, 42, 43, 43, 43, 44, 44, 45, 45, 46, 46, 46, 47, 47, 48, 48, 49, 49, 49, 50, 50, 51, 51, 51, 52, 52, 53, 53, 54, 54, 54, 55, 55, 56, 56, 57, 57, 57, 58, 58, 59, 59, 60, 60, 60, 61, 61, 62, 62, 62, 63, 63, 64, 64, 65, 65, 66, 66, 66, 67, 67, 68, 68, 70, 71, 73, 75, 77, 79, 80, 82, 84, 86, 88, 90, 92, 93, 95, 97, 99, 101, 102, 104, 106, 108, 110, 111, 113, 115, 117, 119, 120, 122, 124, 126, 128, 129, 131, 133, 135, 137, 138, 140, 142, 144, 145, 147, 149, 151, 153, 154, 156, 158, 160, 162, 163, 165, 167, 169, 171, 172, 174, 176, 178, 180, 181, 183, 184, 185, 187, 188, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 237, 239, 240, 241, 242, 243, 244, 245, 246, 248, 249, 250, 251, 252, 253, 254, 254 ]
soslab_g = [ 18, 19, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50, 52, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 69, 71, 72, 74, 75, 77, 78, 80, 81, 83, 84, 86, 88, 89, 91, 92, 94, 95, 97, 98, 100, 101, 103, 105, 106, 108, 109, 111, 112, 114, 116, 117, 118, 119, 120, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 196, 197, 198, 199, 200, 201, 202, 203, 204, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 247, 248, 249, 250, 251, 252, 253, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255 ]
soslab_b = [ 107, 108, 109, 110, 111, 112, 113, 114, 114, 115, 116, 117, 118, 119, 120, 120, 121, 122, 123, 124, 125, 126, 126, 127, 128, 129, 130, 131, 132, 132, 133, 134, 135, 136, 137, 138, 138, 139, 140, 141, 142, 143, 144, 144, 145, 146, 147, 148, 149, 150, 151, 151, 152, 153, 154, 155, 156, 157, 157, 158, 159, 160, 161, 162, 162, 163, 163, 163, 164, 164, 164, 164, 165, 165, 165, 166, 166, 166, 167, 167, 167, 168, 168, 168, 169, 169, 169, 169, 170, 170, 170, 171, 171, 171, 172, 172, 172, 173, 173, 173, 174, 174, 174, 174, 175, 175, 175, 176, 176, 176, 177, 177, 177, 178, 178, 178, 179, 179, 179, 179, 180, 180, 180, 181, 181, 181, 182, 182, 181, 180, 179, 178, 177, 175, 175, 174, 172, 171, 170, 169, 168, 167, 166, 165, 164, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 123, 121, 120, 119, 118, 117, 116, 115, 114, 113, 111, 109, 107, 105, 104, 102, 100, 98, 96, 95, 93, 91, 89, 88, 86, 84, 82, 81, 79, 77, 75, 73, 72, 70, 68, 66, 65, 63, 61, 59, 58, 56, 54, 52, 51, 49, 47, 45, 43, 42, 40, 38, 36, 35, 33, 31, 29, 28, 26, 24, 22, 21, 19, 17, 15, 13, 12, 10, 8, 6, 5, 2, 1, 1 ]

def init_platform():
    """
    Load libsoslab binaries for the current platform.
    """    
    import sys, platform, os
    from ctypes import windll

    # check environment
    libpath = "./"

    if "Windows" == platform.system():
        if "AMD64" == platform.machine():
            if (os.path.isfile(libpath + "lib/libsoslab_core-x64-Release.dll")):
                windll.LoadLibrary(libpath + "lib/libsoslab_core-x64-Release.dll")
                windll.LoadLibrary(libpath + "lib/libsoslab_ml-x64-Release.dll")
                windll.LoadLibrary(libpath + "lib/boost_python3-vc140-mt-1_62.dll")
                windll.LoadLibrary(libpath + "lib/boost_python-vc140-mt-1_62.dll")
            else:
                libpath = libpath + "./parsing/" 
                windll.LoadLibrary(libpath + "lib/libsoslab_core-x64-Release.dll")
                windll.LoadLibrary(libpath + "lib/libsoslab_ml-x64-Release.dll")
                windll.LoadLibrary(libpath + "lib/boost_python3-vc140-mt-1_62.dll")
                windll.LoadLibrary(libpath + "lib/boost_python-vc140-mt-1_62.dll")
    else:
        print("Unsupported platform : %s - %s" % (platform.system(), platform.machine()))
        exit(-1)

    print("Platform : %s - %s" % (platform.system(), platform.machine()))
    sys.path.append(libpath)
    # 여기서는 특정 라이브러리를 로드한다. 이 라이브러리들은 Windows 운영체제에서만 로드되며, 
    # AMD64 아키텍처에 대해서만 지원됨.
    
def parsing_ml(data_path, save_path, sampling):
    import libsoslab_ml_python

    sampling = int(sampling)

    if len(data_path) < 1:
        data_path = "../data.bin"
    if len(save_path) < 1:
        save_path = "./"
    if sampling < 1:
        sampling = 1

    # 여기서는 soslab_ml 모듈의 함수를 사용하여 Lidar 데이터를 파싱하고 PCD(Point Cloud Data)로 변환.

def parsing_lidar_data(data_path, save_path, sampling):
    init_platform()
    parsing_ml(data_path, save_path, sampling)




# 커맨드라인 인자들을 정의하고 파싱합니다. 각각 bin 파일의 경로,
# pcd 파일의 경로 및 샘플링 수를 나타냄.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p1', '--bin-path', help="Path to the bin file", required=False, default="../data.bin")
    parser.add_argument('-p2', '--pcd-path', help="Path to the pcd file", required=False, default="../parsing_bin")
    parser.add_argument('-s', '--sampling', help="number of sampling number", required=False, default="10")

    args = vars(parser.parse_args())

    bin_path = args['bin_path']
    pcd_path = args['pcd_path']
    sampling = args['sampling']
  
  # 위에서 정의한 함수들을 호출하여 Lidar 데이터 파싱 및 변환 작업을 수행.

    init_platform()
    parsing_ml(bin_path,pcd_path,sampling)
        
    print('\nDone.')
