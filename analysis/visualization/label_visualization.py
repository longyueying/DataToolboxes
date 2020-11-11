import matplotlib.pyplot as plt
import numpy as np


def label_distribution(input_path='../../result/label_analysis.txt'):
    label_names = []
    label_quantities = []
    with open(input_path) as f:
        for line in f.readlines():
            label_name, label_quantity = line.strip().split(',')
            label_names.append(label_name)
            label_quantities.append(int(label_quantity))
    # 排序
    label_names = np.asarray(label_names)
    label_quantities = np.asarray(label_quantities)
    label_index = np.argsort(-label_quantities)
    label_names = label_names[label_index]
    label_quantities = label_quantities[label_index]
    # 显示
    plt.figure(figsize=(9, 6))
    plt.gcf().subplots_adjust(bottom=0.2)
    # plt.ylim(0, 2000)
    plt.xticks(rotation=90)
    plt.plot(label_names, label_quantities, marker='.')
    plt.show()


if __name__ == "__main__":
    label_distribution()