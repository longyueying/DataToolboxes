import os
import xml.etree.ElementTree as ET


def box_size_analysis(root_path, classes):
    # initialization
    path_queue = [root_path]
    img_quantity = 0

    # traverse root path
    while path_queue:
        current_path = path_queue.pop(0)
        for item in os.listdir(current_path):
            item = os.path.join(current_path, item)
            if os.path.isdir(item):
                path_queue.append(item)
            # quantity of each annotation class
            elif item.split('.')[-1].lower() == "xml":
                with open(item, encoding="utf-8") as file:
                    label_quantity_image = 0
                    tree = ET.parse(file)
                    tree_root = tree.getroot()
                    for obj in tree_root.iter('object'):
                        cls = obj.find("name").text
                        if classes is None or cls in classes:
                            pass
            # total image number
            elif item.split('.')[-1].lower() in ["jpg", "jpeg", "png"]:
                img_quantity += 1