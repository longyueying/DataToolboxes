import os
import xml.etree.ElementTree as ET


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
    class_select_filenames = []

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
                    flag = False
                    for obj in tree_root.iter('object'):
                        cls = obj.find("name").text
                        if classes is None or cls in classes:
                            flag = True
                            label_quantity_per_class.setdefault(cls, 0)
                            label_quantity_per_class[cls] += 1
                            label_quantity_image += 1
                    label_quantity_per_image.append(label_quantity_image)
                if flag:
                    filename = item.split('\\')[-1].split('/')[-1].split('.')[0]
                    class_select_filenames.append(filename)
            # total image number
            elif item.split('.')[-1].lower() in ["jpg", "jpeg", "png"]:
                img_quantity += 1
    with open("./results/class_select_result.txt", "w") as f:
        for filename in class_select_filenames:
            f.write(filename + '\n')
    print(img_quantity)
    for item in sorted(label_quantity_per_class.items(), key=lambda k: k[1], reverse = True):
        print("{}:{}".format(item[0], item[1]))


if __name__=="__main__":
    label_analysis("D:/biandian/Annotations", ['yw_gkxfw'])
