from utils.image_util import *
from utils.xml_util import *


def xml_matching_inspect(root_path_list, annotations_folder='Annotations', images_folder='JPEGImages'):
    xml_without_image_list = []
    for path, name in xml_path_generator(root_path_list):
        xml_path = os.path.join(path, name)
        image_path = path.replace(annotations_folder, images_folder)
        image_name = name.replace('.xml', '.jpg')
        image_path = os.path.join(image_path, image_name)
        if not os.path.exists(image_path):
            xml_without_image_list.append(xml_path)
    return xml_without_image_list


def image_matching_inspect(root_path_list, annotations_folder='Annotations', images_folder='JPEGImages'):
    image_without_xml_list = []
    for path, name in image_path_generator(root_path_list):
        image_path = os.path.join(path, name)
        xml_path = path.replace(images_folder, annotations_folder)
        xml_name = name.replace('.jpg', '.xml').replace('.JPG', '.xml')
        xml_path = os.path.join(xml_path, xml_name)
        if not os.path.exists(xml_path):
            image_without_xml_list.append(image_path)
    return image_without_xml_list


if __name__ == "__main__":
    for file in image_matching_inspect(["E:/Data/shudian/201912-wuhan/导地线"], annotation_folder='xml', jpegimage_folder='jpg'):
        print(file)
