import os
import xml.etree.ElementTree as ET
from analysis.visualization.pie import Pie
import numpy as np


def label_analysis(root_path, classes=None):
    """
    :param root_path:
    :param classes:
    :return:
    """
    # initialization
    path_queue = [root_path]
    img_quantity = 0
    label_quantity_per_class = {}
    label_quantity_per_image = []

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
                            label_quantity_per_class.setdefault(cls, 0)
                            label_quantity_per_class[cls] += 1
                            label_quantity_image += 1
                    label_quantity_per_image.append(label_quantity_image)
            # total image number
            elif item.split('.')[-1].lower() in ["jpg", "jpeg", "png"]:
                img_quantity += 1
    print("this folder has {} total".format(img_quantity))
    label_quantity_per_image = np.asarray(label_quantity_per_image)
    print("{} images contain required label".format(len(label_quantity_per_image[label_quantity_per_image > 0])))
    pie_graph = Pie()
    pie_graph.pic_for_dict(label_quantity_per_class)
    for item in sorted(label_quantity_per_class.items(), key=lambda k: k[1], reverse = True):
        print("{}:{}".format(item[0], item[1]))


if __name__ == "__main__":
    label_analysis("E:/Data/biandian/2019-biandian-9029", classes=["jsxs"])
