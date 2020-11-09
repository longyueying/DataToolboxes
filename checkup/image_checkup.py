from utils.image_util import image_path_generator
import os
from PIL import Image
from PIL import ImageFile
from tqdm import tqdm
from analysis.data.image_analysis import get_image_number
import piexif
import xml.etree.ElementTree as ET
import cv2 as cv
import numpy as np
from cv2 import IMREAD_COLOR


def valid_checkup(root_path_list):
    broken_list = []
    length = get_image_number(root_path_list)

    for path, name in tqdm(image_path_generator(root_path_list), total=length):
        image_path = os.path.join(path, name)
        try:
            with open(image_path, 'rb') as f:
                value_buf = f.read()
            img_np = np.frombuffer(value_buf, np.uint8)
            img = cv.imdecode(img_np, IMREAD_COLOR)
            cv.cvtColor(img, cv.COLOR_BGR2RGB, img)
            # if img.shape is None:
            #     sub_root_path = path[:path.find(path.split("\\")[-1].split('/')[-1]) - 1]
            #     name = name.split('.')[0]
            #     broken_list.append(f'{sub_root_path},{name}')
        except Exception:
            sub_root_path = path[:path.find(path.split("\\")[-1].split('/')[-1])-1]
            name = name.split('.')[0]
            broken_list.append(f'{sub_root_path},{name}')
    with open("../result/checkup_broken_images.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(broken_list))
    print("There are {}/{} images broken".format(len(broken_list), length))


def postfix_checkup(root_path_list):
    postfix_invalid_list = []
    length = get_image_number(root_path_list)

    for path, name in tqdm(image_path_generator(root_path_list), total=length):
        if not name.split('.')[-1].lower() in ['jpg', 'jpeg']:
            sub_root_path = path[:path.find(path.split("\\")[-1].split('/')[-1]) - 1]
            name = name.split('.')[0]
            postfix_invalid_list.append(f'{sub_root_path},{name}')
    with open("../result/postfix_invalid_images.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(postfix_invalid_list))
    print("There are {}/{} images have invalid postfix".format(len(postfix_invalid_list), length))


def orientation_tag_checkup(root_path_list):
    length = get_image_number(root_path_list)

    for path, name in tqdm(image_path_generator(root_path_list), total=length):
        img_path = os.path.join(path, name)
        img = Image.open(img_path)
        if "exif" in img.info:
            try:
                exif_dict = piexif.load(img.info["exif"])
                if piexif.ImageIFD.Orientation in exif_dict['0th']:
                    orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
                    if orientation != 1:
                        exif_dict['Exif'][41729] = b'1'
                        exif_bytes = piexif.dump(exif_dict)
                        img.save(img_path, exif=exif_bytes)
            except:
                print(img_path)


def size_checkup_fix(root_path_list, annotations_folder='Annotations', images_folder='JPEGImages'):
    length = get_image_number(root_path_list)
    wrong_annotations = []
    for path, name in tqdm(image_path_generator(root_path_list), total=length):
        image_path = os.path.join(path, name)
        xml_path = path.replace(images_folder, annotations_folder)
        xml_name = name.replace('.jpg', '.xml').replace('.JPG', '.xml')
        xml_path = os.path.join(xml_path, xml_name)
        with open(xml_path, encoding='utf-8') as f:
            tree = ET.parse(f)
            tree_root = tree.getroot()
            size_element = tree_root.find('size')
            xml_width = size_element.find('width').text
            xml_height = size_element.find('height').text
        with Image.open(image_path) as im:
            img_width, img_height = im.size
        if not (int(xml_width) == img_width and int(xml_height) == img_height):
            size_element.find('width').text = str(img_width)
            size_element.find('height').text = str(img_height)
            tree.write(xml_path)
        with open(xml_path, encoding='utf-8') as f:
            tree = ET.parse(f)
            tree_root = tree.getroot()
            for obj in tree_root.iter('object'):
                bndbox_element = obj.find("bndbox")
                xmin = int(bndbox_element.find('xmin').text)
                xmax = int(bndbox_element.find('xmax').text)
                ymin = int(bndbox_element.find('ymin').text)
                ymax = int(bndbox_element.find('ymax').text)
                if xmin < 0 or xmax > int(xml_width) or ymin < 0 or ymax > int(xml_height):
                    sub_root_path = path[:path.find(path.split("\\")[-1].split('/')[-1]) - 1]
                    name = name.split('.')[0]
                    wrong_annotations.append(f'{sub_root_path},{name}')
                    break
    # 输出统计信息
    print(f"{len(wrong_annotations)}/{length} files have wrong annotation")
    # 写入文件
    with open("../result/select_by_classes.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(wrong_annotations))



if __name__ == "__main__":
    # ImageFile.LOAD_TRUNCATED_IMAGES = True
    # postfix_checkup(["G:/hongwai/data/VOCdevkit/VOC2007"])
    # orientation_tag_checkup(["E:/训练数据/biandian/diyipi"])
    # valid_checkup(["E:/TrainData/biandian/diyipi"])
    size_checkup_fix(["E:/TrainData/biandian/diyipi"])