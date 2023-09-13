import argparse  # 커맨드라인 인자를 파싱하기 위한 라이브러리
import sys
import os

# 현재 작업 디렉토리에 있는 parsing, process, viz 디렉토리를 sys.path에 추가한다.
sys.path.append(os.getcwd() + "/parsing")
sys.path.append(os.getcwd() + "/process")
sys.path.append(os.getcwd() + "/viz")

# 위에서 추가한 path에서 모듈을 임포트한.
import parsing.parser as soslab_parser
import process.point_cloud_process as process

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # 커맨드라인 인자들을 정의합니다. 각각 bin 파일의 경로, pcd 파일의 경로, 샘플링 수,
    # 파싱 실행 여부, 데이터 처리 실행 여부를 나타냄.
    parser.add_argument('-p1', '--bin-path', help="Path to the bin file", required=False, default="./driving.bin")
    parser.add_argument('-p2', '--pcd-path', help="Path to the pcd file", required=False, default="./parsing_bin")
    parser.add_argument('-s', '--sampling', help="number of sampling number", required=False, default="10")
    
    parser.add_argument('-p', '--parsing', help="Parsing", type=str,required=False, default='True')
    parser.add_argument('-d', '--processing', help="Data processing", type=str, required=False, default='True')

    args = vars(parser.parse_args())
    
    # 각 인자들을 변수에 할당한다.
    bin_path = args['bin_path']
    pcd_path = args['pcd_path']
    sampling = args['sampling']

    parsing_run = args['parsing']
    process_run = args['processing']
    
    # 만약 파싱이 True라면 (즉 사용자가 파싱을 원한다면), Lidar 데이터를 파싱하고 샘플링하는 함수를 실행한다.
    if parsing_run == 'True':
            print("Parsing / Sampling Raw Data")
            soslab_parser.parsing_lidar_data(bin_path ,pcd_path , int(sampling))
            
    # 만약 데이터 처리가 True라면 (즉 사용자가 데이터 처리를 원한다면), 포인트 클라우드 데이터 처리 함수를 실행한다.
    if process_run == 'True':
            print("Point cloud process")
            process.run(args)

