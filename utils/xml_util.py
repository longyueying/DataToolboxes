import xml.etree.ElementTree as ET
import os


def xml_path_generator(root_path):
    """
    :param root_path:
    :return: prefix of xml file and elementTree root
    """
    path_queue = [root_path]
    # traverse root path
    while path_queue:
        current_path = path_queue.pop(0)
        for item in os.listdir(current_path):
            current_name = item
            item = os.path.join(current_path, item)
            if os.path.isdir(item):
                path_queue.append(item)
            elif item.split('.')[-1].lower() == "xml":
                yield current_path, current_name


def classes_mapping(root_path, mapping_dict, signature):
    for current_path, xml_name in xml_path_generator(root_path):
        target_path = current_path + '_' + signature
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        else:
            source_file = os.path.join(current_path, xml_name)
            target_path = os.path.join(target_path, xml_name)
            with open(source_file, "r", encoding="utf-8") as f:
                pass



if __name__ == "__main__":
    classes_mapping("E:/Data/biandian/2019-biandian-1936/Annotations", {}, "e")