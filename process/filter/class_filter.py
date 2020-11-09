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
    root_path_list = ["E:/训练数据/biandian/diyipi/Annotations"]
    target_path = "E:/训练数据/biandian/diyipi/filter"
    cls = ['bj_bpmh', 'bj_bpps', 'bj_wkps', 'jyz_lw', 'jyz_pl', 'sly_bjbmyw', 'sly_dmyw',
           'jsxs', 'hxq_gjtps', 'hxq_yfps', 'xmbhyc', 'yw_gkxfw', 'yw_nc', 'mcqdmsh', 'gbps',
           'gbqs', 'gjptwss', 'bmwh', 'dthtps', 'yxdghsg',
           'yxcr', 'wcaqm', 'wcgz', 'wpdaqs', 'xy', 'rydd', 'hzyw', 'sndmjs', 'qmls', 'wdls', 'xdwcr',
           'bjdsyc', 'ywzt_yfyc', 'ywzt_ywzsjyc', 'hxq_gjbs', 'kgg_ybh', 'kgg_ybf']

    filter_classes(root_path_list, target_path, cls)