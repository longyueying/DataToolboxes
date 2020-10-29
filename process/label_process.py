import xml.etree.ElementTree as ET
from tqdm import tqdm
from utils.xml_util import xml_path_generator
from utils.xml_util import *


def rm_point_line(root_path_list):
    for path, name in tqdm(xml_path_generator(root_path_list), total=get_xml_number(root_path_list)):
        xml_path = os.path.join(path, name)
        with open(xml_path, encoding='utf-8') as f:
            tree = ET.parse(f)
            tree_root = tree.getroot()
            for obj in tree_root.iter('object'):
                bndbox_element = obj.find('bndbox')
                xmin = int(bndbox_element.find('xmin').text)
                ymin = int(bndbox_element.find('ymin').text)
                xmax = int(bndbox_element.find('xmax').text)
                ymax = int(bndbox_element.find('ymax').text)
                if xmin == xmax or ymin == ymax:
                    tree_root.remove(obj)
            tree.write(xml_path)


if __name__ == "__main__":
    rm_point_line(["E:/训练数据/shudian/daodixian/daodixian_total"])