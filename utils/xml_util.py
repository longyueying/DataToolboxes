import xml.etree.ElementTree as ET
import os


def elementTree_generator(root_path):
    """
    :param root_path:
    :return: prefix of xml file and elementTree root
    """
    path_queue = [root_path]
    # traverse root path
    while path_queue:
        current_path = path_queue.pop(0)
        for item in os.listdir(current_path):
            item = os.path.join(current_path, item)
            if os.path.isdir(item):
                path_queue.append(item)
            # quantity of each annotation class
            elif item.split('.')[-1].lower() == "xml":
                xml_prefix = item.split('\\')[-1].split('/')[-1].split('.')[0]
                with open(item, encoding="utf-8") as file:
                    tree = ET.parse(file)
                    tree_root = tree.getroot()
            yield xml_prefix, tree_root
