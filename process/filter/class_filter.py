import os
import xml.etree.ElementTree as ET
import shutil
from utils.xml_util import xml_path_generator


def filter_classes(root_path_list, target_path, classes):
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    os.makedirs(target_path)
    for folder_path, filename in xml_path_generator(root_path_list):
        ori_file_path = os.path.join(folder_path, filename)
        target_file_path = os.path.join(target_path, filename)
        tree = ET.parse(ori_file_path)
        tree_root = tree.getroot()
        for obj in tree_root.findall('object'):
            cls = obj.find("name").text
            if cls not in classes:
                tree_root.remove(obj)
        tree.write(target_file_path)


if __name__ == "__main__":
    root_path_list = ["E:/训练数据/shudian/daodixian_total"]
    target_path = "E:/训练数据/shudian/daodixian_total/jzpy_anno_daodixian_jzpy_filter"
    classes = ['daodixian_01', 'daodixian_02', 'daodixian_05']

    filter_classes(root_path_list, target_path, classes)