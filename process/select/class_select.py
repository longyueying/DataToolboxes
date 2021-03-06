import os
import xml.etree.ElementTree as ET
from tqdm import tqdm
from utils.xml_util import xml_path_generator
from analysis.data.label_analysis import get_xml_number


def select_by_classes(root_path_list, classes=None):
    # 初始化
    root_path_list = root_path_list.copy()
    xml_number_total = get_xml_number(root_path_list)
    xml_selected_list = []
    # 遍历xml文件
    for path, name in tqdm(xml_path_generator(root_path_list), total=xml_number_total):
        xml_path = os.path.join(path, name)
        with open(xml_path, encoding='utf-8') as f:
            tree = ET.parse(f)
            tree_root = tree.getroot()
            flag_select = False
            for obj in tree_root.iter('object'):
                cls = obj.find("name").text
                if classes is None or cls in classes:
                    flag_select = True
                    break
            if flag_select:
                sub_root_path = path[:path.find(path.split("\\")[-1].split('/')[-1]) - 1]
                name = name.split('.')[0]
                xml_selected_list.append(f'{sub_root_path},{name}')
    # 输出统计信息
    print(f"{len(xml_selected_list)}/{xml_number_total} files have be selected")
    # 写入文件
    with open("../../result/select_by_classes.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_selected_list))


if __name__ == "__main__":
    # labels = [
    #     "010000021",
    #     "010000022",
    #     "010000023",
    #     "010100061",
    #     "010300091",
    #     "010000031",
    #     "010001011",
    #     "010002051",
    #     "010003021",yw_gkxfw
    #     "010100041",
    #     "010101021",
    #     "010200051",
    #     "010201011"]
    # select_by_classes(["E:/Data/shudian/wgs_5-7/jy202007/算法培育202007/杆塔",
    #                    "E:/Data/shudian/wgs_5-7/jy202005/0605数据库导出/杆塔"], labels)
    # select_by_classes(["E:/测试数据/shudian/dingwei"], ['daodixian_01', 'daodixian_02', 'daodixian_05'])
    cls = ['bj_bpmh', 'bj_bpps', 'bj_wkps', 'jyz_lw', 'jyz_pl', 'sly_bjbmyw', 'sly_dmyw',
           'jsxs', 'hxq_gjtps', 'hxq_yfps', 'xmbhyc', 'yw_gkxfw', 'yw_nc', 'mcqdmsh', 'gbps',
           'gbqs', 'gjptwss', 'bmwh', 'dthtps', 'yxdghsg',
           'yxcr', 'wcaqm', 'wcgz', 'wpdaqs', 'xy', 'rydd', 'hzyw', 'sndmjs', 'qmls', 'wdls', 'xdwcr',
           'bjdsyc', 'ywzt_yfyc', 'ywzt_ywzsjyc', 'hxq_gjbs', 'kgg_ybh', 'kgg_ybf']
    select_by_classes(["E:/Data/biandian/2020-biandian-liangpi/第一批"], cls)