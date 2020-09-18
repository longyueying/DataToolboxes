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
    labels = ['ganta1']
    select_by_classes(["E:/训练数据/shudian/ganta", "E:/训练数据/shudian/jueyuanzi"], labels)