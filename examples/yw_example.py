from utils.file_util import *

tongdao_txt_path = "../process/select/results/tongdao_select_result.txt"
tongdao_source_annotations_path = "E:/Data/yiwu/tongdao/Annotations"
tongdao_source_images_path = "E:/Data/yiwu/tongdao/JPEGImages"

biandian_txt_path = "../process/select/results/biandian_select_result.txt"
biandian_source_annotations_path = "E:/Data/yiwu/biandian/yw_gkxfw/Annotations"
biandian_source_images_path = "E:/Data/yiwu/biandian/yw_gkxfw/JPEGImages"

delete_txt_path = "../process/select/results/del_select_result.txt"
target_annotations_path = "../process/tmp/Annotations"
target_images_path = "../process/tmp/JPEGImages"

cp_files(tongdao_txt_path, tongdao_source_annotations_path, tongdao_source_images_path,
         target_annotations_path, target_images_path, rm_origin_path=True)
cp_files(biandian_txt_path, biandian_source_annotations_path, biandian_source_images_path,
         target_annotations_path, target_images_path)
delete_files(delete_txt_path, target_annotations_path, target_images_path)