from utils.image_util import image_path_generator
import os
import shutil
import json
import xml.etree.ElementTree as ET
from tqdm import tqdm


def image_matching_inspect(root_path_list):
    image_without_xml_list = []
    for path, name in image_path_generator(root_path_list):
        image_path = os.path.join(path, name)
        xml_path = os.path.join(path, "xml")
        xml_name = name.replace('.jpg', '.xml').replace('.JPG', '.xml')
        xml_path = os.path.join(xml_path, xml_name)
        if not os.path.exists(xml_path):
            image_without_xml_list.append(image_path)
    return image_without_xml_list


def create_jpg_folder(root_path_list):
    for path, name in image_path_generator(root_path_list):
        jpg_folder = os.path.join(path, "jpg")
        if not os.path.exists(jpg_folder):
            os.mkdir(jpg_folder)
        img_ori_path = os.path.join(path, name)
        img_target_path = os.path.join(jpg_folder, name)
        shutil.move(img_ori_path, img_target_path)


def merge_xml(json_file, save_folder,  annotations_folder='Annotations', images_folder='JPEGImages'):
    with open(json_file) as f:
        dup_data = json.load(f)

    for _, v in tqdm(dup_data.items(), total=len(dup_data.keys())):
        base_path, base_img_name = v[0]
        base_xml_name = base_img_name.split('.')[0] + '.xml'
        base_xml_path = base_path.replace(images_folder, annotations_folder)
        base_xml_path = os.path.join(base_xml_path, base_xml_name)
        if len(v) > 1:
            name_list = [base_xml_name]
            with open(base_xml_path) as f:
                tree_base = ET.parse(f)
                root_element_base = tree_base.getroot()

            for path, img_name in v[1:]:
                xml_name = img_name.split('.')[0] + '.xml'
                name_list.append(xml_name)
                xml_path = path.replace(images_folder, annotations_folder)
                xml_path = os.path.join(xml_path, xml_name)
                with open(xml_path) as f:
                    tree = ET.parse(f)
                    root_element = tree.getroot()
                    for obj in root_element.iter('object'):
                        root_element_base.append(obj)

            for filename in set(name_list):
                filepath = os.path.join(save_folder, filename)
                tree_base.write(filepath)
        else:
            target_xml_path = os.path.join(save_folder, base_xml_name)
            shutil.copy(base_xml_path, target_xml_path)


if __name__ == "__main__":
    # for img in image_matching_inspect(["E:/Data/shudian/wgs_5-7"]):
    #     print(img)
    # create_jpg_folder(["E:/Data/shudian/wgs_5-7"])
    merge_xml("../result/new_dup_hash.json", "E:/test", annotations_folder='xml_voc', images_folder='jpg')