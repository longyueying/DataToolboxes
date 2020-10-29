from utils.image_util import image_path_generator
import os
from PIL import Image
from tqdm import tqdm
from analysis.data.image_analysis import get_image_number
import piexif
import xml.etree.ElementTree as ET


def valid_checkup(root_path_list):
    broken_list = []
    length = get_image_number(root_path_list)

    for path, name in tqdm(image_path_generator(root_path_list), total=length):
        image_path = os.path.join(path, name)
        try:
            Image.open(image_path)
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
    orientation_tag_detected_list = []
    length = get_image_number(root_path_list)

    for path, name in tqdm(image_path_generator(root_path_list), total=length):
        img_path = os.path.join(path, name)
        img = Image.open(img_path)
        print(img_path)
        try:
            exif_dict = piexif.load(img.info["exif"])
            orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
            if orientation != 1:
                print("{}:{}".format(orientation, img_path))
                orientation_tag_detected_list.append(img_path)
        except Exception:
            pass
            #print("{} occured some wrong".format(img_path))
    with open("../result/rotated_images.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(orientation_tag_detected_list))


def size_checkup_fix(root_path_list, annotations_folder='Annotations', images_folder='JPEGImages'):
    length = get_image_number(root_path_list)
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


if __name__ == "__main__":
    # postfix_checkup(["G:/hongwai/data/VOCdevkit/VOC2007"])
    # orientation_tag_checkup(["E:/训练数据/shudian/daodixian/daodixian_total"])
    # valid_checkup(["G:/hongwai/data/VOCdevkit/VOC2007"])
    size_checkup_fix(["E:/训练数据/shudian/daodixian/daodixian_total"])