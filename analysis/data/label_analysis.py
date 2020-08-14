from analysis.visualization.pie import Pie
from utils.xml_util import *
from tqdm import tqdm
from utils.xml_util import xml_path_generator


def get_xml_number(root_path_list):
    root_path_list = root_path_list.copy()
    return sum(1 for _, _ in xml_path_generator(root_path_list))


def label_classes_analysis(root_path_list, classes=None, plot_pie=False):
    # 初始化
    root_path_list = root_path_list.copy()
    label_quantity_per_class = {}
    xml_number_select = 0
    xml_number_total = 0
    # 遍历xml文件
    for path, name in tqdm(xml_path_generator(root_path_list), total=get_xml_number(root_path_list)):
        xml_number_total += 1
        xml_path = os.path.join(path, name)
        with open(xml_path, encoding='utf-8') as f:
            tree = ET.parse(f)
            tree_root = tree.getroot()
            number_of_required_classes = 0
            for obj in tree_root.iter('object'):
                cls = obj.find("name").text
                if classes is None or cls in classes:
                    label_quantity_per_class.setdefault(cls, 0)
                    label_quantity_per_class[cls] += 1
                    number_of_required_classes += 1
            if number_of_required_classes > 0:
                xml_number_select += 1
    # 打印统计信息
    print("{}/{} xmls contain required label".format(xml_number_select, xml_number_total))
    for item in sorted(label_quantity_per_class.items(), key=lambda k: k[1], reverse=True):
        print("{}:{}".format(item[0], item[1]))
    # 绘制扇形图
    if plot_pie:
        pie_graph = Pie()
        pie_graph.pic_for_dict(label_quantity_per_class)


if __name__ == "__main__":
    # label_analysis(["C:/Users/zxh/Desktop/jsxs_gjbs/jsxs_gjbs"], classes=["jsxs", "hxq_gjbs"])
    label_classes_analysis(["E:/Data/shudian/201912-wuhan/导地线"])
